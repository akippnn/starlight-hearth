# ADR-0009 — niri-owned hearthOS Shell lifecycle

**Status:** accepted
**Date:** 2026-08-28

## Context

RC.1 attached the shell to `graphical-session.target`, linked the same units
from `niri.service.wants`, and also started them from niri configuration. The
packaged QML failure was the visible RC.1 defect, but three startup paths also
made ordering, duplicate-start diagnosis, and session teardown unnecessarily
ambiguous.

## Decision

`niri.service` is the single lifecycle owner for hearthOS Shell in Desktop
Mode.

- The image links the companion and UI units from `niri.service.wants`.
- Both units use `PartOf=niri.service`, so leaving or restarting the compositor
  stops or restarts the shell coherently.
- The companion orders after niri and becomes active only after acquiring
  `org.starlight.HearthShell` with `Type=dbus`.
- The UI orders after niri and the companion, requires the companion, and uses
  `Type=exec` so an executable/startup failure is reported synchronously.
- niri configuration does not issue a second `systemctl start` command.
- The five-second readiness gate remains a delivery requirement, not a relaxed
  systemd timeout claim.

## Consequences

Gaming Mode does not run hearthOS Shell. Entering hearthOS Desktop starts one
companion and one Quickshell process through the compositor lifecycle. Leaving
Desktop Mode tears down both while transient application units retain their
separate lifecycle. Emergency keyboard restart continues to target the same
packaged unit names.
