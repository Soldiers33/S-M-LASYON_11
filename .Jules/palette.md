## Palette's Journal

## 2024-03-02 - Initial Setup
**Learning:** Initializing journal for micro-UX tracking.
**Action:** Starting UX improvement process for the command line application interface.

## 2025-03-02 - CLI Loading Bar Polish
**Learning:** Multi-line progress indicators in CLI applications cause terminal clutter and push important historical context off-screen rapidly, making it harder for users to review output.
**Action:** Updated `loading_bar` in Python scripts to use carriage returns (`\r`) with `flush=True` to clear and overwrite the current line, resulting in a significantly cleaner visual experience.

## 2026-03-14 - ANSI Escape Codes for CLI Spinners
**Learning:** Using `\r` (carriage return) with `flush=True` in Python terminal progress indicators is a good start, but it leaves ghost characters if the new line is shorter than the previous line. This creates a messy, confusing user experience during dynamic loading states.
**Action:** Always pair `\r` with the ANSI escape code `\033[K` (erase to end of line) like `\r\033[K` when building in-place CLI loading bars or spinners to ensure complete overwriting of previous text.
