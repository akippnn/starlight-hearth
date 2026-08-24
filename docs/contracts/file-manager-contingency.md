# File-manager contingency

**State:** Accepted contingency; dormant and not a planned replacement
**Activation:** requires failure of existing candidates and a new owner decision

## Current policy

Dolphin remains the default file manager and a core App Menu favorite while
application-profile and controller/keyboard workflow testing proceeds.
Nautilus is the second off-the-shelf candidate. No custom file-manager work is
authorized merely because either application has isolated rough edges.

## Activation gate

Activate a new collision-free `FM-*` delivery track only when:

1. Dolphin and Nautilus have each been evaluated against the required local
   browse/open/copy/move/rename/delete/recovery workflows;
2. neither can satisfy the owner-visible contract with reasonable profiles,
   configuration, or bounded upstream-compatible changes;
3. the result is documented with exact versions and limitations; and
4. the owner explicitly authorizes the contingency before KDE recovery
   retirement.

## Reuse direction if activated

- Fork Index directly and preserve its upstream history; do not create a file
  manager from scratch.
- Retain MauiKit FileBrowsing, KF6, KIO, and useful KDE libraries where they
  reduce risk and satisfy licensing/packaging requirements.
- Study COSMIC Files and other projects only as references unless a later ADR
  selects direct reuse.
- Record exact full revisions and per-file licensing when the contingency is
  activated; the current abbreviated Index research revision is not an import
  pin.

Removing the Plasma shell does not require removing KDE libraries. Dolphin
remains the default until an Index-derived candidate passes every non-owner
gate and receives an explicit owner acceptance verdict.

Fedora package references retained from planning:

- [Index](https://packages.fedoraproject.org/pkgs/maui-mauikit-index-fm/maui-mauikit-index-fm)
- [MauiKit FileBrowsing](https://packages.fedoraproject.org/pkgs/maui-mauikit-filebrowsing/maui-mauikit-filebrowsing)
