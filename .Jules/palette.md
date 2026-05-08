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

## 2026-05-08 - Async Feedback in Vanilla JS UI
**Learning:** Raw HTML/JS templates often lack the robust state management features of modern frameworks like React, making it easy to forget intermediate UI states like loading indicators and disabled states during asynchronous operations like `fetch()`. If `catch` block error handling is omitted, failed fetch requests can result in a broken UI where buttons remain permanently disabled.
**Action:** Always implement a `finally` block or equivalent reset logic in vanilla JS `fetch` chains, ensuring elements like buttons are properly restored (e.g., removing `disabled` attribute, resetting opacity and original text). Additionally, when hiding visual feedback during these states, utilize `aria-live="polite"` to provide accessible context to screen readers regarding the UI state change.
