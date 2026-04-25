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
## 2026-04-25 - Replace blocking alert with async toast
**Learning:** Using synchronous `alert()` in vanilla HTML apps combined with `location.reload()` creates a jarring user experience where visual state changes (like buttons entering a disabled state) may fail to render before the UI freezes.
**Action:** Always prefer using a non-blocking UI update strategy (e.g., toast notification) and a `setTimeout` (like 2000ms) before reloading the page to give users visual feedback and an accessible live announcement.
