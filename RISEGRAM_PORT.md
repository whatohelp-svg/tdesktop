# RiseGram Desktop native port (Windows and Linux)

One native Qt/C++ source tree supports Windows and Linux. The same pinned RiseGram DC2 TCP endpoint and server public RSA key are used by both. Public Telegram fallback and route replacement are disabled. Startup uses a separate RiseGram data directory under Qt GenericDataLocation; old Telegram data migration and portable data discovery are disabled. Do not reuse Telegram session files.

Linux: use docs/building-linux.md and the native Docker toolchain, with your own API credentials and -D DESKTOP_APP_DISABLE_AUTOUPDATE=ON -D DESKTOP_APP_DISABLE_CRASH_REPORTS=ON. Windows: docs/building-win.md with the same flags. Use only test accounts until separate application identity, branding, transport, login/relaunch, media and shared economy integration are tested. No installer or release is implied by this source branch.

## CI builds

The experimental Windows and Linux builds run on pushes to `risegram/native-port`. Check the Actions run for each platform and download its artifact only after a successful build. These are test binaries, not verified installers.

## Current desktop beta limitations
The build now applies the monochrome RiseGram branding and adds +888 to the phone country list. The current source speaks MTProto layer 234; production currently rejects that exact layer. A successful Windows or Linux compilation does not establish login compatibility. Do not distribute as a verified release until a matching schema and real sign-in are tested.
