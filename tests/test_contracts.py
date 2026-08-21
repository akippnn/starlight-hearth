import json
import os
from pathlib import Path
import stat
import subprocess
import tempfile
import textwrap
import tomllib
import unittest


ROOT = Path(__file__).resolve().parents[1]
SYSTEM = ROOT / "files/system"
ADAPTER = SYSTEM / "usr/libexec/hearth-session-mode"
BOOTSTRAP = SYSTEM / "usr/libexec/hearth-session-bootstrap"


def run(command, *, env=None):
    return subprocess.run(
        command,
        cwd=ROOT,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


class SessionAdapterTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        self.sessions = self.root / "sessions"
        self.sessions.mkdir()
        for name in ("hearth.desktop", "plasma.desktop"):
            (self.sessions / name).write_text("[Desktop Entry]\n", encoding="utf-8")
        self.log = self.root / "calls.log"
        self.ctl = self.root / "steamosctl"
        self.ctl.write_text(
            textwrap.dedent(
                """\
                #!/usr/bin/env bash
                set -euo pipefail
                case "${1:-}" in
                  --help)
                    if [[ "${HEARTH_STUB_MODE:-supported}" == "help-fails" ]]; then
                      exit 1
                    elif [[ "${HEARTH_STUB_MODE:-supported}" == "missing-command" ]]; then
                      echo "get-valid-desktop-sessions set-default-desktop-session"
                    else
                      echo "get-valid-desktop-sessions set-default-desktop-session set-default-login-mode switch-to-desktop-mode switch-to-game-mode"
                    fi
                    ;;
                  get-valid-desktop-sessions)
                    if [[ "${HEARTH_STUB_MODE:-supported}" == "query-fails" ]]; then
                      exit 1
                    elif [[ "${HEARTH_STUB_MODE:-supported}" == "missing-session" ]]; then
                      printf 'Sessions:\\n\\n- plasma.desktop\\n'
                    else
                      printf 'Sessions:\\n\\n- gamepadui-with-qam-session.desktop\\n- hearth.desktop\\n- plasma.desktop\\n'
                    fi
                    ;;
                  *)
                    printf '%s\\n' "$*" >> "${HEARTH_STUB_LOG:?}"
                    ;;
                esac
                """
            ),
            encoding="utf-8",
        )
        self.ctl.chmod(0o755)
        self.env = os.environ.copy()
        self.env.update(
            {
                "HEARTH_STEAMOSCTL": str(self.ctl),
                "HEARTH_WAYLAND_SESSIONS_DIR": str(self.sessions),
                "HEARTH_STUB_LOG": str(self.log),
            }
        )

    def tearDown(self):
        self.tempdir.cleanup()

    def calls(self):
        return self.log.read_text(encoding="utf-8").splitlines() if self.log.exists() else []

    def test_desktop_switch_uses_supported_contract(self):
        result = run([str(ADAPTER), "desktop"], env=self.env)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            self.calls(),
            ["set-default-desktop-session hearth.desktop", "switch-to-desktop-mode"],
        )

    def test_gaming_switch_preserves_steam_ownership(self):
        result = run([str(ADAPTER), "gaming"], env=self.env)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            self.calls(),
            [
                "set-default-desktop-session hearth.desktop",
                "set-default-login-mode game",
                "switch-to-game-mode",
            ],
        )

    def test_gaming_return_survives_missing_hearth_session(self):
        self.env["HEARTH_STUB_MODE"] = "missing-session"
        result = run([str(ADAPTER), "gaming"], env=self.env)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("continuing to Gaming Mode", result.stderr)
        self.assertEqual(
            self.calls(),
            ["set-default-login-mode game", "switch-to-game-mode"],
        )

    def test_kde_recovery_is_explicit(self):
        result = run([str(ADAPTER), "recovery-kde"], env=self.env)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            self.calls(),
            ["set-default-desktop-session plasma.desktop", "switch-to-desktop-mode"],
        )

    def test_unknown_upstream_contract_fails_before_mutation(self):
        self.env["HEARTH_STUB_MODE"] = "missing-command"
        result = run([str(ADAPTER), "desktop"], env=self.env)
        self.assertEqual(result.returncode, 2)
        self.assertIn("unsupported steamosctl contract", result.stderr)
        self.assertEqual(self.calls(), [])

    def test_unadvertised_session_fails_before_mutation(self):
        self.env["HEARTH_STUB_MODE"] = "missing-session"
        result = run([str(ADAPTER), "desktop"], env=self.env)
        self.assertEqual(result.returncode, 2)
        self.assertIn("does not advertise", result.stderr)
        self.assertEqual(self.calls(), [])

    def test_failed_upstream_queries_fail_before_mutation(self):
        for mode, message in (
            ("help-fails", "help failed"),
            ("query-fails", "cannot query valid desktop sessions"),
        ):
            with self.subTest(mode=mode):
                self.env["HEARTH_STUB_MODE"] = mode
                result = run([str(ADAPTER), "desktop"], env=self.env)
                self.assertEqual(result.returncode, 2)
                self.assertIn(message, result.stderr)
                self.assertEqual(self.calls(), [])

    def test_missing_tool_and_invalid_invocation_exit_two(self):
        self.env["HEARTH_STEAMOSCTL"] = str(self.root / "missing")
        result = run([str(ADAPTER), "gaming"], env=self.env)
        self.assertEqual(result.returncode, 2)
        result = run([str(ADAPTER), "unknown"], env=self.env)
        self.assertEqual(result.returncode, 2)


class BootstrapTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        self.config = self.root / "config"
        self.state = self.root / "state"
        self.env = os.environ.copy()
        self.env.update(
            {
                "HOME": str(self.root),
                "XDG_CONFIG_HOME": str(self.config),
                "XDG_STATE_HOME": str(self.state),
                "HEARTH_SHARE_DIR": str(SYSTEM / "usr/share/hearth"),
            }
        )

    def tearDown(self):
        self.tempdir.cleanup()

    def test_new_user_receives_versioned_defaults(self):
        result = run([str(BOOTSTRAP)], env=self.env)
        self.assertEqual(result.returncode, 0, result.stderr)
        niri = self.config / "niri/config.kdl"
        settings = self.config / "DankMaterialShell/settings.json"
        marker = self.state / "hearth/session-bootstrap-v1"
        self.assertIn("/usr/share/hearth/niri/hearth.kdl", niri.read_text(encoding="utf-8"))
        self.assertEqual(json.loads(settings.read_text(encoding="utf-8"))["currentThemeName"], "custom")
        self.assertTrue(marker.is_file())
        self.assertEqual(stat.S_IMODE(settings.stat().st_mode), 0o600)

    def test_existing_configuration_is_backed_up_and_not_overwritten(self):
        niri = self.config / "niri/config.kdl"
        settings = self.config / "DankMaterialShell/settings.json"
        niri.parent.mkdir(parents=True)
        settings.parent.mkdir(parents=True)
        niri.write_text("// owner setting\n", encoding="utf-8")
        settings.write_text('{"currentThemeName":"owner"}\n', encoding="utf-8")

        first = run([str(BOOTSTRAP)], env=self.env)
        second = run([str(BOOTSTRAP)], env=self.env)
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(second.returncode, 0, second.stderr)
        content = niri.read_text(encoding="utf-8")
        self.assertTrue(content.startswith("// owner setting"))
        self.assertEqual(content.count("/usr/share/hearth/niri/hearth.kdl"), 1)
        self.assertEqual(
            (self.config / "niri/config.kdl.pre-hearth-v1").read_text(encoding="utf-8"),
            "// owner setting\n",
        )
        self.assertEqual(json.loads(settings.read_text(encoding="utf-8"))["currentThemeName"], "owner")

    def test_existing_backup_is_never_overwritten(self):
        niri = self.config / "niri/config.kdl"
        backup = self.config / "niri/config.kdl.pre-hearth-v1"
        niri.parent.mkdir(parents=True)
        niri.write_text("// current owner setting\n", encoding="utf-8")
        backup.write_text("// earlier owner backup\n", encoding="utf-8")

        result = run([str(BOOTSTRAP)], env=self.env)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(backup.read_text(encoding="utf-8"), "// earlier owner backup\n")
        self.assertIn("/usr/share/hearth/niri/hearth.kdl", niri.read_text(encoding="utf-8"))


class ImageContractTests(unittest.TestCase):
    def test_recipe_keeps_compatibility_and_signing_order(self):
        recipe = (ROOT / "recipes/recipe.yml").read_text(encoding="utf-8")
        self.assertIn("base-image: ghcr.io/ublue-os/bazzite-deck", recipe)
        self.assertIn("blue-build-tag: v0.9.37", recipe)
        self.assertNotIn("blue-build-tag: v0.9.37-installer", recipe)
        self.assertIn("- linux/amd64", recipe)
        self.assertIn("- avengemedia/dms", recipe)
        self.assertIn("- dms", recipe)
        self.assertIn("- niri", recipe)
        self.assertIn("NAME: hearthOS", recipe)
        self.assertIn("VARIANT_ID: hearth", recipe)
        self.assertNotIn("\n      ID:", recipe)
        self.assertNotIn("\n      ID_LIKE:", recipe)
        self.assertNotIn("\n      VERSION_ID:", recipe)
        self.assertLess(recipe.index("- type: os-release"), recipe.index("verify-hearth-image.sh"))
        self.assertLess(recipe.index("verify-hearth-image.sh"), recipe.index("- type: signing"))
        self.assertTrue(recipe.rstrip().endswith("- type: signing"))
        for flatpak in (
            "org.jellyfin.JellyfinDesktop",
            "io.mpv.Mpv",
            "org.localsend.localsend_app",
            "io.github.flattool.Warehouse",
            "io.missioncenter.MissionCenter",
        ):
            self.assertIn(flatpak, recipe)
        self.assertIn("tailscaled.service", recipe)

    def test_public_session_and_recovery_contracts_exist(self):
        session = (SYSTEM / "usr/share/wayland-sessions/hearth.desktop").read_text(encoding="utf-8")
        self.assertIn("Name=Hearth Desktop", session)
        self.assertIn("Exec=/usr/libexec/hearth-session", session)
        justfile = (ROOT / "files/justfiles/hearth.just").read_text(encoding="utf-8")
        self.assertIn("hearth-recovery-kde:", justfile)
        self.assertIn("hearth-return-gaming:", justfile)
        self.assertFalse((SYSTEM / "usr/bin/starlight").exists())

    def test_static_data_is_parseable_and_locked_to_v1(self):
        theme = json.loads((SYSTEM / "usr/share/hearth/themes/hearth.json").read_text(encoding="utf-8"))
        self.assertEqual(theme["dark"]["background"], "#171117")
        self.assertEqual(theme["dark"]["warning"], "#D9A35F")
        manager_path = SYSTEM / "usr/share/steamos-manager/user.d/config.toml"
        self.assertTrue(manager_path.is_file())
        self.assertFalse((SYSTEM / "etc/steamos-manager/config.toml").exists())
        manager = tomllib.loads(manager_path.read_text(encoding="utf-8"))
        self.assertEqual(manager["session"]["desktop"], "hearth.desktop")
        layout = json.loads((ROOT / "tests/fixtures/controller-layout-v1.json").read_text(encoding="utf-8"))
        self.assertEqual(layout["name"], "Hearth Desktop v1")
        self.assertEqual(layout["input_owner"], "steam-input")
        actions = {item["control"]: item for item in layout["actions"]}
        self.assertEqual(actions["menu"]["emits"], "F10")
        self.assertEqual(actions["view"]["emits"], "F9")
        self.assertTrue(actions["guide"]["emits"].startswith("Steam:"))

    def test_scripts_are_syntactically_valid_and_executable(self):
        scripts = [
            ROOT / "files/scripts/configure-hearth-session.sh",
            ROOT / "files/scripts/verify-hearth-image.sh",
            SYSTEM / "usr/libexec/hearth-session",
            BOOTSTRAP,
            ADAPTER,
        ]
        for script in scripts:
            self.assertTrue(os.access(script, os.X_OK), script)
            result = run(["bash", "-n", str(script)])
            self.assertEqual(result.returncode, 0, f"{script}: {result.stderr}")

        bootstrap = BOOTSTRAP.read_text(encoding="utf-8")
        self.assertNotIn("dms setup", bootstrap)
        self.assertNotIn("usermod", bootstrap)
        image_setup = (ROOT / "files/scripts/configure-hearth-session.sh").read_text(encoding="utf-8")
        self.assertIn("/usr/bin/niri validate", image_setup)
        self.assertIn("/usr/bin/dms version", image_setup)

        final_check = (ROOT / "files/scripts/verify-hearth-image.sh").read_text(encoding="utf-8")
        self.assertIn('[[ "${NAME:-}" == "hearthOS" ]]', final_check)
        self.assertIn("rpm -q --qf", final_check)
        self.assertIn("systemctl is-enabled tailscaled.service", final_check)
        self.assertIn("[[ ! -e /usr/bin/starlight ]]", final_check)

    def test_no_mutable_latest_artifact_or_retired_name(self):
        tracked_text = []
        for path in ROOT.rglob("*"):
            if path.is_file() and ".git" not in path.parts and path.suffix in {".yml", ".yaml", ".sh", ".toml", ".desktop", ".just"}:
                tracked_text.append(path.read_text(encoding="utf-8"))
        text = "\n".join(tracked_text)
        self.assertNotIn("/latest/", text)
        self.assertNotIn("starlightOS Hearth", text)


if __name__ == "__main__":
    unittest.main()
