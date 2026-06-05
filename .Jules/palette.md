## Palette's Journal

## 2024-03-02 - Initial Setup
**Learning:** Initializing journal for micro-UX tracking.
**Action:** Starting UX improvement process for the command line application interface.

## 2025-03-02 - CLI Loading Bar Polish
**Learning:** Multi-line progress indicators in CLI applications cause terminal clutter and push important historical context off-screen rapidly, making it harder for users to review output.
**Action:** Updated `loading_bar` in Python scripts to use carriage returns (`\r`) with `flush=True` to clear and overwrite the current line, resulting in a significantly cleaner visual experience.

## 2026-03-20 - CLI Loading Bar Polish
**Learning:** Using `\r` to overwrite lines in the CLI leaves "ghost characters" if the new text is shorter than the old text. This creates a confusing reading experience. Adding `\033[K` (erase to end of line) ensures a clean overwrite.
**Action:** Implemented `\r\033[K` in the `loading_bar` function in `simulasyon_11.py` with a final `\n` to prevent overlap on subsequent terminal outputs.
## 2025-03-09 - Animated Braille Spinner for CLI Progress
**Learning:** Terminal output needs dynamic visual cues. Simple static text (e.g. `Loading...`) is ambiguous as to whether the process is frozen or just slow. Using an animated Braille character spinner with carriage return (`\r`) and erase-to-end-of-line (`\033[K`) ANSI codes provides a smooth, accessible indication of asynchronous operation without cluttering the screen buffer.
**Action:** Use animated terminal spinners across long-running Python CLI scripts to improve progress observability.
