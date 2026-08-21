# Current status

Last updated: 2026-08-21

This is the single current-status source for `starlight-hearth`.

## Active slice

**VS-001 — Controller-Ready Hearth Desktop** is **active**.

Implemented at image-content revision
`ed70d875e132f5bf814da8302dea1740d324f7af` and contract-suite revision
`685a3c4bdd733d51c003a9533577d915a383b37b`:

- hearthOS `os-release` identity while preserving the Bazzite/Fedora compatibility fields;
- niri and DMS installation through Fedora/COPR packaging;
- `Hearth Desktop`, DMS user-service integration, warm defaults, and frozen controller actions;
- fail-closed `steamosctl` session switching and KDE/Gaming Mode recovery entrypoints;
- removal of the stale `starlight` stub and replacement of the broken justfiles state;
- local adapter, bootstrap, image-contract, and controller-fixture tests;
- a final in-image verifier for identity, packages, session wiring, Tailscale policy, and stale-stub absence.

## Verification state

| Gate | State | Evidence |
|---|---|---|
| Repository contract tests | Pass | 16 tests on macOS and x86_64 Bazzite on 2026-08-21 |
| BlueBuild schema expansion | Pass | BlueBuild 0.9.37 on x86_64; corrected Containerfile SHA-256 `6337f4afccb96e42f6b855189a0f67cff1ec17a62637684be64ef58091ebbfe6` |
| Complete OCI image build | Pending | No candidate digest recorded |
| Built-image package/session inspection | Pending | Requires candidate image |
| Living-room PC owner audit | Pending | Passwordless SSH available; candidate and physical controller proof still required |
| Owner acceptance | Pending | Owner-only verdict |

The slice is not `audit-ready` and is not `accepted`. The next blocking evidence
is a complete image build. The booted base is cached in OSTree, but unprivileged
export to rootless Podman is denied; CI or a one-time owner-authorized root export
is required before package/version capture and the physical controller/session audit.

## Known limitations

- Steam Input layout creation remains an explicit owner step in Steam's UI.
- Controller grades are intentionally unassigned until tested on the target receiver/controller.
- The exact DMS and niri NEVRAs and candidate OCI digest must come from the completed image build.
- DMS is a bridge; there is no Hearth Shell runtime yet.
- Decky Loader and Framegen are not part of this slice.
