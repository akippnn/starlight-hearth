# ADR-0008 — Documentation and delivery governance

**Status:** accepted
**Date:** 2026-08-25

## Decision

Use the following decision lifecycle for planning records:

- `Proposed` — source requirement or candidate direction not yet chosen;
- `Accepted` — explicitly chosen by the owner but still reopenable;
- `Frozen-for-slice` — approved at an exact revision for one implementation
  slice;
- `Superseded` — replaced while retaining provenance;
- `Open` — a material choice that has not been made.

No item becomes `Frozen-for-slice` merely because it appears in an ADR or
behavior contract. Product delivery uses one canonical loop:

`roadmap → frozen slice contract → evidence → current status → owner audit`

Roadmap, contract, evidence, and current status have distinct authority.
Delivery state and owner verdict remain separate. Only the owner may record an
accepted product outcome.

Preserve immutable handoffs, historical contracts, rejected candidates, and
partial passing evidence. Correct mutable public claims through current docs
instead of rewriting history. Never reuse a historical slice identifier for a
different outcome.

## Current documentation phase

The 2026-08-25 reconciliation is documentation only. No product slice is
active, frozen, implemented, deployed, audit-ready, or owner-accepted as a
result of this work. Future IDs remain provisional until their contracts are
planned and approved.
