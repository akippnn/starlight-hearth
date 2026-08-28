# Controller compatibility planning register

**State:** no active candidate and no current compatibility verdict

Record compatibility only against an exact application/package/image revision
and a declared owner workflow. A source test or generic reputation does not
establish an application grade.

## Grades

- **A — native semantic:** purpose-built focus/actions with correct hints.
- **B — native application/focus:** complete through the application's reliable
  gamepad or keyboard focus behavior.
- **C — pointer/profile assisted:** complete with explicit Hearth profile,
  pointer, and supported OSK behavior.
- **D — unsupported:** requires an undeclared physical-keyboard workaround or
  cannot complete the required workflow.

## Future evaluation inventory

| Surface/application | Required workflow | Target | Current evidence |
| --- | --- | --- | --- |
| Hearth session transition | Gaming → Desktop → Gaming, reconnect, recovery | A/B | Historical partial evidence only |
| App Menu | Open, focus, search, change Grid/List, launch, context action, close | A | HSN-002 proposed; no candidate |
| hearthOS System Bar | Reveal, focus, open/close owned panel, restore focus | A | No hearthOS-native candidate |
| OSK | Open, type, change layer/layout, dock, secure field, close | A | No wvkbd-derived candidate |
| hearthOS Settings | Navigate and apply/recover one setting | A | Proposed |
| hearthOS Portal | Inspect and execute one typed safe action | A | Proposed |
| KDE recovery | Enter recovery, perform essential workflow, return | A–C | Historical recovery evidence; remains required |
| Firefox | Browse, URL/text entry, download | A–C | Candidate-specific audit required |
| Dolphin | Browse, open, copy/move/rename/delete/recover | A–C | Default retained; contingency gate requires evidence |
| Nautilus | Same file workflow if evaluated as fallback | A–C | Not yet evaluated |
| Other default applications | Workflow from the accepted application catalog | A–C | Exact candidate required |

A future default-application outcome must define how D grades are handled; it
cannot silently publish unsupported applications as controller-friendly.
The file-manager activation rule is in
`docs/contracts/file-manager-contingency.md`.
