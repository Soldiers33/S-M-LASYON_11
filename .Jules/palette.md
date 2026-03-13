## Palette's Journal

## 2024-03-02 - Initial Setup
**Learning:** Initializing journal for micro-UX tracking.
**Action:** Starting UX improvement process for the command line application interface.

## 2025-03-02 - CLI Loading Bar Polish
**Learning:** Multi-line progress indicators in CLI applications cause terminal clutter and push important historical context off-screen rapidly, making it harder for users to review output.
**Action:** Updated `loading_bar` in Python scripts to use carriage returns (`\r`) with `flush=True` to clear and overwrite the current line, resulting in a significantly cleaner visual experience.

## 2025-03-13 - CLI Progress Indicators Ghosting
**Learning:** Using only a carriage return (`\r`) in a CLI loop overwrites text from the beginning of the line but does not erase trailing characters if the new string is shorter than the old one, leading to confusing "ghost" text artifacts.
**Action:** Combined `\r` with the ANSI escape code `\033[K` (erase to end of line) whenever implementing single-line progress indicators to ensure previous, longer text is completely removed.
