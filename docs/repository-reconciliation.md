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

## Deferred reconciliation

The future shell repository operation must separately:

1. reconfirm and archive every ref and dirty input;
2. choose the private archive repository name;
3. establish clean Hearth-native canonical history;
4. selectively import only reviewed implementation and tests;
5. record every donor revision/license;
6. perform the hard runtime rename through a frozen product slice; and
7. leave recovery available throughout.

This record authorizes none of those steps.
