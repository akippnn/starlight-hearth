# Current status

**Last updated:** 2026-08-29
**Current phase:** HIN-001 implementation
**Active implementation slice:** HIN-001
**New owner verdict:** HSN-001 accepted

This is the single mutable delivery-status authority for `starlight-hearth`.

## Current work

The documentation foundation is clean at
`6b544e02c3c9a70985b886672482e92c135032f3`. The owner approved
`HSN-001 — hearthOS Launcher Nucleus`; its active v2 contract is frozen at
`43ca3393adf1dbbc2448ea8bfbfddc80761f386f`. Immutable v1 remains byte-for-byte
unchanged at `17fedae8776ff38b53c07d4098d8ee8b13852253`.

HSN-001 delivery state is `closed`; owner verdict is `accepted`. RC.1 remains
released at signed tag `hearth-v0.3.0-rc.1`, source revision
`a3503dc734cab9111b065691609bc339918bd779`. Fedora package, real user-bus,
native QtDBus/M3Shapes, and source/static checks pass. Product integration
revision `87faf5525fc8de4b39e7a1241eca04b05bb05823` pins its immutable RPM URL and
SHA-256. BlueBuild run `32813973301` passed at clean build head
`ae04d4fe93ce8c65cb928b30229099c1f6766f99`, producing signed OCI index
`sha256:e1791f4ba537c0d052b704d4aaff2f168244b63f3d013f372952c8fd90765372`.
Independent Cosign verification passed on `aki@hearth`, and the owner later
booted that exact index. The RC.1 field smoke proved controller and keyboard
navigation plus Return to Gaming Mode, but found packaged UI startup, pointer,
application-launch lifecycle, layout, scrim, icon, and performance defects.
The earlier shell commits through `3bfe0f4c` and product commit `ee6b158` were
unreleased RC.2 inputs. They are superseded as candidate identities by the
clean revisions recorded below. Recovery, exact signed-image proof, and owner
audit remain pending.

The preserved v11 checkpoint met its performance target but failed Launcher
Presentation because the selection contour remained faceted and its fade was
sequenced incorrectly. It is explicitly recorded as a visual failure rather
than a successful candidate.

The replacement RC.2 staging tree now proves the corrected transient
application lifecycle, closed-state activation rejection, service-restart
survival, visible invalid-config fallback, visible launch failure, real icons,
and bounded two-endpoint icon behavior. One preallocated native scene-graph
surface uses M3Shapes device-pixel antialiasing, morphs the compact contour to a
rounded rectangle before tone/bounds expansion, and owns one dark restrained
elevation. Real-niri screenshots cover Grid/List at logical 1920x1080 and
1280x720. Fifty rapid changes rendered at p95/p99/max `16/16/17 ms`; 30
panel/view cycles rendered at `1/16/17 ms`, with a `182.7 MiB` peak.

A task-labeled Fedora 44 build passed Rust, user-bus, QML/offscreen, native
bridge, contract, payload, dependency, license, no-DMS, and network-disabled
offline-install checks. Its local RPM SHA-256 is
`463f6409247eafecd9a13e5226bb27f08192cc03cd541db0ccafa1d85f0d5cf9`.
It is local evidence only, not a published RC.2 identity.

The current shell candidate is clean and pushed at
`38059d5b03705e8a663e191cf1cd4a6a753ada6b` on
`codex/hsn-001-launcher-nucleus`. It makes niri the sole owner of companion/UI
startup and teardown. A real Gaming Mode-to-Desktop transition started the
companion about 61 ms and the UI about 72 ms after niri; Quickshell completed
configuration loading in about 548 ms with `Input1.Ready=true` and one UI
process. The task-labeled transition setup was removed afterward.
The local product integration is clean at image-changing commit `dc6e746`,
with the hashed evidence checkpoint recorded through
`ddffa30ebff25b832468816b0a2b547d4b06512f` on the matching feature branch.

The subsequent RC.2 build/package gate was intentionally interrupted at the
owner's request before a new build process or container was running. Inspection
confirmed that no task-labeled builder required termination; caches, build
artifacts, and unrelated processes were left untouched. The requested shared
native selection increment and resumed local package gate are complete at an
evidence-recorded engineering checkpoint.

The owner authorized promotion to the RC.2 live image. This was authorization
to integrate and deploy that exact candidate, not an HSN-001 acceptance
verdict.
Shell Fedora verification run `33098257890` and RPM run `33098257814` passed at
the exact candidate revision. Signed tag `hearth-v0.3.0-rc.2` and the sole main
RPM asset are published; the asset SHA-256 is
`02084a8f3197d34553088464e0d4321a484c04c4c841ee998c0388d88437f1e3`.
Public `main`, final `hearth-v0.3.0`, and owner verdict remain unchanged.

The owner then rebased and rebooted `aki@hearth` to signed OCI index
`sha256:dea09a20687b3f235b0dd89f817a3a63dcbc24499d1dfa6fa34a813af8f6b191`.
The deployment and automatic hearthOS Shell startup passed. Field inspection
found a gray frosted drawer-sized surface while the launcher was closed. The
image applied its compositor-wide xray fallback to the normal always-warm
drawer namespace, so the complete layer was blurred after Quickshell cleared
the shaped region.

The correction is clean locally at shell revision
`b17c1bb582090fa2aa294c29a7e97e3b2e5ac3ea` and product revision
`30fb91dd0ddf1de2ad4afe473663ca789aea5644`. Real-niri staging removed the
artifact across 30 open/close plus Grid/List cycles at p95/p99/max
`13/19/19 ms`, with stable peak memory, no measured mesh allocations, and no
QML warnings. Packaged services were restored after testing; the booted RC.2
therefore still contains the defect.

A subsequent owner field evaluation on that booted RC.2 passed controller,
keyboard, physical-pointer, controller-pointer, Grid/List, external-launch,
shell-restart survival, receiver reconnect, and Return to Gaming Mode
workflows. The initial teardown snapshot preceded the owner's return action;
the later overlapping trace ended with Gamescope active and niri plus both
shell units stopped, so it does not establish a session-lifecycle defect.

The historical field wording called LB the primary click. HSN-001 v2 records
the approved physical order as RB primary/left click and LB secondary/right
click. The ambiguous physical-click and cross-repository mapping-compatibility
proof are invalidated and must be rerun on the next signed candidate; all
other field, lifecycle, launch, reconnect, performance, blur, and presentation
evidence retains its recorded identity.

The same evaluation found a second blocking presentation defect: cards and the
Grid/List selector can show competing selection, hover, press, and uncontained
ripple shapes. Clean local shell revision
`f80b365ebda1d4f226918f76328375e25cb52969` repairs the shared interaction
primitives: pointer hover immediately retargets the one canonical controller/
keyboard selection through the native sliding/morphing surface, and activation
adds at most one contained ripple/deformation. macOS and Fedora suites pass;
real-niri selection and panel/view workloads both measured p95/p99/max
`16/16/16 ms`, with stable peak memory and no QML warnings. At that checkpoint
HSN-001 remained `active/pending`; RC.3 later packaged the repair and received
the accepted owner verdict recorded below. The over-eager invisible right-edge hover anchor is
nonblocking for HSN-001 and is allocated to the future System Bar, where a
generous click target will surround the visible App Menu button.

The owner superseded the combined-train delivery hold on 2026-08-29 and
authorized HSN-001 to proceed independently through an RC.3 package, signed
image, target rebase, owner audit, and—only after explicit acceptance—public
`main` promotion. This authorization is limited to the frozen HSN-001 v2
outcome and its existing blur, unified-selection, and physical bumper-mapping
repairs. That directive did not itself authorize later slices or infer an
HSN-001 verdict. The owner subsequently accepted RC.3 and separately authorized
HIN-001 on 2026-08-30. Product
`3c88f23f9f341e4e812baec653eb3f3fdb628a26` and shell
`f80b365ebda1d4f226918f76328375e25cb52969` remain preserved local evidence
checkpoints rather than audit targets; the exact clean RC.3 inputs replaced
them as candidate identities. HSN-001 is `closed/accepted`. HIN-001 is
authorized for an exact freeze and implementation; HSN-002 and HIN-002 remain
`proposed/pending` with no candidates or implementation authority. Their
decision-complete review material keeps outcomes separate:
HIN-001 owns headless hold/chord routing, HSN-002 owns App Menu and the first
reusable `InputHintBar`, and HIN-002 owns visible niri-backed latches. No exact
revision is approved or frozen yet.

The clean RC.3 shell source is published at
`e2ff2e564fb17e4123eafe1378dc90e7fb10b914`. Fedora verification run
`33250142200` and RPM run `33250142134` pass. Signed tag
`hearth-v0.3.0-rc.3` resolves to that exact revision, and its sole main RPM
asset has SHA-256
`89895cc2ab05435c7496e5192132b6195892394c2e7eb44caac01b27e4cf4763`.
The clean product candidate is
`c91a45516259c2de404c8cb809efda3f1fdd69d2`. BlueBuild run `33250710107`
passed contracts, image verification, build, publication, and workflow Cosign
verification. Signed OCI index
`sha256:0cc5b33733a601c34aa31f7ee026d7f373ba14a6b1b766710f8b6aea4f3a0c96`
contains linux/amd64 manifest
`sha256:539cbb319712c24d9c96af34a16ce5967dde30b0214d6dcdfc5420c3f6c0962b`;
independent registry identity inspection agrees. Exact details and evidence
reuse are recorded in the
[RC.3 image checkpoint](evidence/artifacts/hsn-001-rc3-image-c91a455/RESULTS.md).
The target later booted that exact index and manifest with the RC.3 RPM and
both shell units active. The owner accepted the candidate while recording the
motion/color limitations and skipped physical bumper repeat in
[the RC.3 owner audit](evidence/artifacts/hsn-001-rc3-owner-audit/RESULTS.md).

R3/L3 are packaged navigation/manipulation defaults rather than immutable
controls. The proposed router and hint contracts keep semantic layers separate
from physical bindings so hold and latch triggers can differ; later Controller
Settings may remap every action and create safe custom modifiers. View/Select
is allocated to future System Bar focus with Control Center initially selected.
Base LT/RT and Guide+LT/RS/LB/RB remain free.

## Superseded phase statement

The complete 2026-08-24 handoff and later planning decisions were
reconciled into canonical product, architecture, requirement, decision,
behavior, roadmap, and open-question documents. This work changes
documentation only.

It does **not**:

- freeze or activate a product slice;
- implement hearthOS Shell, App Menu, Bar, OSK, Settings, Portal, wallpaper, or
  Gaming Mode behavior;
- change the OCI image, packages, configuration, InputPlumber, niri, deployed
  host, or `starlight-hearth-shell` repository;
- create an audit target;
- claim audit-readiness or owner acceptance.

## Historical status

| Record | Delivery state | Owner verdict | Current interpretation |
| --- | --- | --- | --- |
| VS-001 / HS-001 | Superseded | Rejected for controller-ready outcome | Boot, identity, TV-scale, niri/DMS startup, and recovery evidence remain historical facts. |
| VS-002 / HS-002 | Superseded | Not accepted | Input/session handoff and packaging evidence remain useful; it did not establish an accepted controller-native desktop. |
| HS-003 | Superseded | Pending/no owner verdict | Feature-branch implementation evidence exists; no owner-visible Hearth-native result is claimed. |

The old DMS-derived-product decision is superseded by ADR-0006. The semantic
controller architecture remains reusable under ADR-0007. Historical ADRs,
contracts, and evidence retain their original wording and must be interpreted
through these newer authorities.

## Accepted planning decisions

- Hearth-owned Quickshell/QML shell on unmodified niri.
- DMS as selective reference/donor, not maintained product.
- `GPL-3.0-only` shell governance with an exact import ledger.
- Rust companion plus QML UI, transient application launches, and layered JSON
  configuration.
- Explicit Navigation/Text modes and current semantic input defaults.
- Right-drawer App Menu with exactly Grid/List modes.
- wvkbd-derived OSK architecture and privacy/geometry/input behavior.
- hearthOS System Bar visible for hover, focus, or any owned open panel.
- Dolphin retained with a dormant Index/MauiKit file-manager contingency.
- Explicit decision lifecycle and owner-only product acceptance.

These are accepted and reopenable planning decisions. None is
`Frozen-for-slice`.

## Repository and deployment state

The documentation work began from `starlight-hearth` `main` at
`aec9dc874da5c4c698ca74073fc087f449454e74`. The former dirty HS-003 worktree
was preserved in its branch, a named Git stash, and an external verified
archive before switching to `main`.

The historical DMS refs and dirty state remain preserved in the private archive
recorded by repository reconciliation. Public shell and product `main` branches
remain unchanged; HSN-001 work lives on dedicated feature branches and signed
candidate tags. Product revision `79eae57e…` passed BlueBuild run
`33144073834`. Its signed index is `sha256:dea09a…`, its amd64 manifest is
`sha256:d1af12…`, and independent Cosign verification passed on `aki@hearth`.
The host now boots that exact RC.2 index and retains the previous RC.1
deployment as rollback. The local blur correction is not installed in the
booted deployment.

Existing image/build metadata may still project historical VS-002 state. The
HSN-001 RC.3 authorization permits a new image only after those non-document
public projections are reconciled against this status; later-slice images
still require their own explicit delivery greenlight.

## Next gate

Implement HIN-001 against frozen v1 contract
`bd93779fc4388df968796d90955578af8e30da79`, accepted product baseline
`be2da6c0972e549584bbf6e6211261cf69a817bd`, and accepted shell baseline
`e2ff2e564fb17e4123eafe1378dc90e7fb10b914`. Prove the router/domain,
canonical/derived manifests, real niri provider, system providers, package,
and authentic target progressively. HSN-002 and HIN-002 remain proposed and
unauthorized; the RC.3 owner findings are planning inputs only.
