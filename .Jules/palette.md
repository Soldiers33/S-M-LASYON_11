## Palette's Journal

## 2024-03-02 - Initial Setup
**Learning:** Initializing journal for micro-UX tracking.
**Action:** Starting UX improvement process for the command line application interface.

## 2025-03-02 - CLI Loading Bar Polish
**Learning:** Multi-line progress indicators in CLI applications cause terminal clutter and push important historical context off-screen rapidly, making it harder for users to review output.
**Action:** Updated `loading_bar` in Python scripts to use carriage returns (`\r`) with `flush=True` to clear and overwrite the current line, resulting in a significantly cleaner visual experience.

## 2026-03-17 - CLI Loading Bar Ghost Character Fix
**Learning:** Using `\r` alone to clear terminal lines can leave "ghost characters" if the new string is shorter than the old one, and omitting a final newline can cause subsequent terminal outputs to overlap or format incorrectly.
**Action:** Added the ANSI escape code `\033[K` (erase to end of line) after `\r` to clear ghost characters, and ensured the final `print` command includes an explicit newline (`\n`) to preserve clean formatting for subsequent console outputs.
