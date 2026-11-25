# RiseGram Desktop native port (Windows and Linux)

One native Qt/C++ source tree supports Windows and Linux. The same pinned RiseGram DC2 TCP endpoint and server public RSA key are used by both. Public Telegram fallback and route replacement are disabled. Startup uses a separate RiseGram data directory under Qt GenericDataLocation; old Telegram data migration and portable data discovery are disabled. Do not reuse Telegram session files.

Linux: use docs/building-linux.md and the native Docker toolchain, with your own API credentials and -D DESKTOP_APP_DISABLE_AUTOUPDATE=ON -D DESKTOP_APP_DISABLE_CRASH_REPORTS=ON. Windows: docs/building-win.md with the same flags. Use only test accounts until separate application identity, branding, transport, login/relaunch, media and shared economy integration are tested. No installer or release is implied by this source branch.
