# Repository reconciliation record

**Record date:** 2026-08-25
**Scope:** documentation preparation only

## Preserved product feature state

Before returning the primary `starlight-hearth` worktree to `main`, the
following state was observed:

- branch `codex/hs-003-controller-app-menu`;
- HEAD `2e9cb4559b338d36877edd375cbf7bc386a55868`;
- modified `README.md`;
- untracked `docs.zip`;
- untracked `docs/game-compatibility.md`.

It remains recoverable through the original branch and stash commit
`7db150a70929dcbfccb285c80392a32ce6c66d19`. The named stash was created as:

`pre-documentation-foundation 2026-08-25 codex/hs-003-controller-app-menu`

An additional local archive exists at:

`/Users/akippnn/Projects/10 Projects/hearth-recovery-snapshots/2026-08-25-before-documentation-foundation/`

| Artifact | SHA-256 |
| --- | --- |
| `feature-worktree.tar.gz` | `fa437d60a634cf60df69b840b3bce00ede0dc27bcee9df2b83a8db0fcdce4ac5` |
| `all-refs-with-stash.bundle` | `2a20edc99dd7d0ca21840e93d73c28cb63521aa2d5e254e73177b3312317405e` |

The Git bundle was verified and contains the feature branch, `main`, other
captured refs, and `refs/stash`. The tar preserves the pre-stash worktree
outside `.git`.

## Documentation base

The primary product worktree was switched to local `main`, fast-forward checked
against `origin/main`, and based on:

`aec9dc874da5c4c698ca74073fc087f449454e74`

Unique HS-003 ADR/contract/evidence documents were copied verbatim from the
preserved feature branch so their historical record is not lost. No
implementation source was merged.

## Untouched repositories and worktrees

The separate Gaming Mode worktree remained on
`codex/gm-001-low-latency-gaming-mode` at
`95c827ae23ef755dbcd07cb8cd49b94d6270f61f`. Its identifier conflicts with a
later Hearth Portal/apps proposal and must not be reused.

`starlight-hearth-shell` was not mutated. At inspection it had:

- local `main` at `49456632b17ba962755c2dd18376d9a859eaf11a`;
- `origin/main` at `16ee3a209396caba209c8604fb70eeb8ca182f7f`;
- local `main` 19 commits behind;
- an existing dirty `dank-qml-common` submodule state and `.DS_Store` artifacts;
- full DMS ancestry on the current canonical history.

The deployed host was not changed by this documentation work.

## HSN-001 shell archive result

The owner-authorized archive operation completed before HSN-001 shell work:

- private remote: `akippnn/starlight-hearth-shell-dms-archive`;
- verified all-refs bundle: `starlight-hearth-shell-all-refs.bundle`, SHA-256
  `b874ff99e9ee25fd8f5ab638c5744923b67137488299065603f293ddaf59ed15`;
- dirty worktree snapshot: `starlight-hearth-shell-dirty-worktree.tar.gz`,
  SHA-256
  `9233da1d728ef2e0867e68b3aa622e4715e7feed2c7f06d962a0f168fe40c924`;
- bundle verification: complete history, 133 refs including symbolic remote
  HEAD; remote verification: 132 concrete refs with sampled main, HS-003,
  release-tag, and remote-tracking identities matching;
- recovery directory:
  `/Users/akippnn/Projects/10 Projects/hearth-recovery-snapshots/2026-08-25-hsn-001-shell-archive/`;
- clean orphan worktree:
  `/Users/akippnn/Projects/10 Projects/starlight-hearth-shell-hsn001`, branch
  `codex/hsn-001-launcher-nucleus`.

The existing public `main`, historical tags, and original dirty worktree were
not changed.

## Remaining reconciliation

The future shell repository operation must separately:

1. build and inspect the clean Hearth-native candidate package;
2. record every final donor file/license and installed notice;
3. prove the hard runtime rename in the built image;
4. leave recovery available throughout; and
5. cut over public `main` only after owner acceptance and separate authorization.

This record authorizes none of those steps.
