# Architecture decision index

ADRs record decisions in their historical context. Their `Status` lines are
not product-slice verdicts. Later ADRs supersede only the stated portions;
`docs/status.md` remains the current delivery authority.

| ADR | Current interpretation |
| --- | --- |
| ADR-0001 | Historical and superseded; initial DMS/Steam Input foundation. |
| ADR-0002 | Historical. Repository separation, pinned artifacts, fail-safe input ownership, and recovery remain useful; DMS-as-product and compatibility requirements are superseded by ADR-0006/0007. |
| ADR-0003 | Historical HS-003 decision. Semantic routing remains reusable under ADR-0007; DMS-derived-product policy is superseded by ADR-0006. |
| ADR-0004 | Historical InputPlumber mouse-button implementation contract; no current controller mapping is frozen from it. |
| ADR-0005 | Historical multi-track/application strategy. Owner-only acceptance and replacement-before-removal remain; future IDs/order and blanket OSK rejection are superseded or reopened. |
| ADR-0006 | Current accepted shell/reuse/license direction. |
| ADR-0007 | Current accepted runtime/configuration/OSK boundaries. |
| ADR-0008 | Current accepted documentation and delivery governance. |
