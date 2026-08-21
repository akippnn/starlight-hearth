# Current status

Last updated: 2026-08-21

This is the single current-status source for `starlight-hearth`.

## Active slice

**VS-001 — Controller-Ready Hearth Desktop** is **active**.

Implemented at image-content revision
`ed70d875e132f5bf814da8302dea1740d324f7af` and contract-suite revision
`685a3c4bdd733d51c003a9533577d915a383b37b`, with the first image-build
repair at `fb18d9f16c17072c1aa54bb2d97c4f92a499692a` and successful candidate
revision `16664ab9e824a50afdb80bd530b39f7c8997d0d0`:

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
| Complete OCI image build | Pass | Run `32495095478` at `16664ab9e824a50afdb80bd530b39f7c8997d0d0`; candidate `sha256:fa97f83ee9daddf9f3dd11302d3510e750aecec1ed31a2b88981ac791fa2eb01` |
| Built-image package/session inspection | Pass at build time | Final verifier completed; niri `26.04-1.fc44`, DMS `1.5.3-1.fc44`, Xwayland Satellite `0.8.2-1.fc44`; candidate signature verified from x86_64 Bazzite |
| Living-room PC owner audit | Pending | Passwordless SSH available; candidate and physical controller proof still required |
| Owner acceptance | Pending | Owner-only verdict |

The slice is not `audit-ready` and is not `accepted`. The next blocking evidence
is the owner audit of this immutable candidate on the living-room PC, including
controller compatibility grades and repeated Gaming↔Desktop transitions.

## Known limitations

- Steam Input layout creation remains an explicit owner step in Steam's UI.
- Controller grades are intentionally unassigned until tested on the target receiver/controller.
- The exact DMS/niri NEVRAs and candidate OCI digest are recorded; live DMS IPC and controller grades remain unproven.
- DMS is a bridge; there is no Hearth Shell runtime yet.
- Decky Loader and Framegen are not part of this slice.
