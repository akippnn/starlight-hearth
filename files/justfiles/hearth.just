# hearthOS recovery entrypoints. These call a fail-closed adapter that validates
# the current steamos-manager contract before changing session state.

[doc('Switch to the KDE recovery desktop')]
hearth-recovery-kde:
    /usr/libexec/hearth-session-mode recovery-kde

[doc('Return to Steam Gaming Mode')]
hearth-return-gaming:
    /usr/libexec/hearth-session-mode gaming

[doc('Switch to Hearth Desktop')]
hearth-desktop:
    /usr/libexec/hearth-session-mode desktop
