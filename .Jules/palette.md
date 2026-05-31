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

## 2026-03-02 - Vanilla HTML/JS Toast UX
**Learning:** In vanilla HTML templates like `index.html` (which is loaded dynamically in `dashboard_11.py`), using `display: none` to completely hide toast notifications is much more accessible than visually hiding them while keeping them in the tree. Delaying reload actions or restoring button states in async `fetch().finally()` ensures users see success/error feedback clearly without becoming permanently disabled.
**Action:** Always implement explicit `.catch()` and `.finally()` on async UX features, and use ARIA-live attributes rather than block-level alerts for micro-UX updates.
