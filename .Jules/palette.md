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

## 2026-05-27 - Button Loading State Micro-UX
**Learning:** For asynchronous actions in simple vanilla JavaScript templates that don't have a reactive state library, long-running processes (like scanning a file system) without clear inline UI feedback often cause multiple clicks and user frustration.
**Action:** When updating such components, always add an `id`, `aria-live="polite"`, visually disable the button, and use `.finally()` in `fetch` calls to guarantee the UI unlocks regardless of the success/failure state of the request.
