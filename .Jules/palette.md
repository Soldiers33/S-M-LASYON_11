## Palette's Journal

## 2024-03-02 - Initial Setup
**Learning:** Initializing journal for micro-UX tracking.
**Action:** Starting UX improvement process for the command line application interface.

## 2025-03-02 - CLI Loading Bar Polish
**Learning:** Multi-line progress indicators in CLI applications cause terminal clutter and push important historical context off-screen rapidly, making it harder for users to review output.
**Action:** Updated `loading_bar` in Python scripts to use carriage returns (`\r`) with `flush=True` to clear and overwrite the current line, resulting in a significantly cleaner visual experience.

## 2026-03-19 - CLI Progress Bar Ghost Characters
**Learning:** When using carriage returns (`\r`) to update a CLI line in-place, shorter subsequent strings leave "ghost" characters from previous longer strings if the line isn't explicitly cleared. Furthermore, the final success state must retain a newline to prevent subsequent terminal output from colliding with the final status.
**Action:** Appended the ANSI escape code `\033[K` immediately after `\r` to clear the line to the end, preventing ghost characters. The final print call was kept with its default newline (`\n`) behavior.
