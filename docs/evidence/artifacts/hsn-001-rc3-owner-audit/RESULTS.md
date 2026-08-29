# HSN-001 RC.3 owner audit

Date: 2026-08-30
Target: `aki@hearth`, Fedora 44, owner 8BitDo Pro 3 cohort

## Exact audit target

- Product image source: `c91a45516259c2de404c8cb809efda3f1fdd69d2`
- Shell source: `e2ff2e564fb17e4123eafe1378dc90e7fb10b914`
- OCI index: `sha256:0cc5b33733a601c34aa31f7ee026d7f373ba14a6b1b766710f8b6aea4f3a0c96`
- Booted amd64 manifest: `sha256:539cbb319712c24d9c96af34a16ce5967dde30b0214d6dcdfc5420c3f6c0962b`
- Installed RPM: `hearth-shell-0.3.0-0.3.rc3.fc44.x86_64`
- RPM SHA-256: `89895cc2ab05435c7496e5192132b6195892394c2e7eb44caac01b27e4cf4763`

Target-side registry resolution and Cosign/Rekor verification passed before
deployment. After reboot, `rpm-ostree status --json` identified the exact index
and manifest as booted, the RC.3 RPM was installed, and
`hearth-shell.service` plus `hearth-shell-ui.service` were active.

## Owner result

The owner observed the corrected animation candidate, recorded the motion and
color findings in the canonical evidence record, and explicitly accepted
HSN-001: “HSN-001 is good.”

Physical RB/LB behavior was not separately repeated in this audit message; the
accepted capability boundary retains that limitation.
