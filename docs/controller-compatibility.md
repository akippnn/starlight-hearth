# VS-004 application compatibility matrix

Status: deferred; not an acceptance gate for VS-002

Record grades only when VS-004 is active and after exercising its exact candidate with the owner's
2.4 GHz receiver and Xbox-style logical mapping. A row needs a grade, observed
workflow, candidate digest, and notes before it counts as evidence.

| Surface/application | Required workflow | Target | Observed grade | Evidence/notes |
|---|---|---:|---:|---|
| Gaming → Hearth Desktop | Steam Power menu, session starts, controller remains active | A/B | Pending | Candidate required |
| DMS launcher | Open, move focus, launch, close | A/B | Pending | Candidate required |
| DMS Control Center | Volume, brightness, network, Bluetooth | A/B | Pending | Candidate required |
| Return to Gaming Mode | Launch action and regain Steam UI | A/B | Pending | Candidate required |
| KDE recovery | Run `ujust hearth-recovery-kde`, navigate, return | A/B | Pending | Candidate required |
| Polkit prompt | Focus identity/password, use OSK, authorize/cancel | A/B | Pending | Candidate required |
| Steam on-screen keyboard | Open, enter text, close, restore focus | A/B | Pending | Candidate required |
| Firefox | Browse, focus controls, enter URL/text, download | A–C | Pending | Candidate required |
| Dolphin | Browse locations, open/copy/move one file, close | A–C | Pending | Candidate required |
| Jellyfin Desktop | Browse, search with OSK, play/pause/seek, exit | A–C | Pending | Candidate required |
| mpv | Open media, play/pause/seek, fullscreen, exit | A–C | Pending | Candidate required |
| LocalSend | Select device/file, send/receive, acknowledge result | A–C | Pending | Candidate required |
| Warehouse | Inspect an app and a non-destructive setting | A–C | Pending | Candidate required |
| Mission Center | Navigate views, inspect a process, close | A–C | Pending | Candidate required |

A D result in any row blocks audit-readiness unless the application is removed
from the default set in a separately reviewed change.
