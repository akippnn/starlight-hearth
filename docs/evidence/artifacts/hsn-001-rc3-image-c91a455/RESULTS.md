# HSN-001 RC.3 signed-image checkpoint

- Frozen contract: HSN-001 v2 at product revision
  `43ca3393adf1dbbc2448ea8bfbfddc80761f386f`.
- Shell source: `e2ff2e564fb17e4123eafe1378dc90e7fb10b914`;
  signed tag `hearth-v0.3.0-rc.3`.
- Shell verification: Fedora runs `33250142200` and `33250142134` passed.
- Sole RC.3 release asset:
  `hearth-shell-0.3.0-0.3.rc3.fc44.x86_64.rpm`, SHA-256
  `89895cc2ab05435c7496e5192132b6195892394c2e7eb44caac01b27e4cf4763`.
- Product source: `c91a45516259c2de404c8cb809efda3f1fdd69d2`.
- BlueBuild run `33250710107` passed product contracts, image verification,
  build, publication, and workflow Cosign verification.
- OCI index: `sha256:0cc5b33733a601c34aa31f7ee026d7f373ba14a6b1b766710f8b6aea4f3a0c96`.
- Linux amd64 manifest:
  `sha256:539cbb319712c24d9c96af34a16ce5967dde30b0214d6dcdfc5420c3f6c0962b`.
- Provenance attestation manifest:
  `sha256:d2a9fbabb00a8ac6768d3079e7dc0f0fd00a9c5c75395b65090c2ed5f43c6b1e`.
- Rekor log index: `2636896426`.

An independent anonymous GHCR manifest read confirmed that immutable tag
`c91a455-44` resolves to the recorded OCI index and contains the recorded
linux/amd64 and attestation manifests. The preceding product attempt at
`e90b3c6a…` failed because its image verifier still required the defective
normal-drawer blur namespace. Product revision `c91a4551…` corrects that stale
assertion and guards both the required xray fallback and absence of the old
normal-drawer rule.

A deterministic comparison of the exact product and shell
`inputplumber-v4.json` mirrors passed: `RightBumper=pointer-primary` and
`LeftBumper=pointer-secondary`. Both repositories' contract suites also pass.
This proves source compatibility only; it does not replace the physical
signed-candidate controller test.

The frozen contract, Rust service behavior, session/application lifecycle, and
recovery procedures are unchanged. Their immutable RC.2 evidence remains
applicable where exact source and procedure are unchanged. The RC.3 shell
workflows reran provider, consumer, package, and direct-contract checks because
the package and candidate claim changed. Existing real-niri evidence at shell
`b17c1bb5…`/product `30fb91dd…` for the blur repair and shell `f80b365e…` for
unified selection exercises the same code contained in RC.3; signed-image
target confirmation remains required.

This is a signed-image checkpoint, not an audit-ready or accepted result.
Target-side RPM inspection, rebase/boot, physical RB-primary/LB-secondary
proof, cross-repository mapping confirmation, owner motion review, and the
formal owner verdict remain pending. `aki@hearth` was unreachable over SSH
during candidate preparation, so no RC.3 target claim is made.
