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
## 2026-05-01 - Replaced blocking alerts with async toast notifications
**Learning:** In vanilla JavaScript/HTML templates without a CSS framework, replacing synchronous blocking `alert()` dialogues with asynchronous toast notifications (`role="status"`) alongside explicitly visually disabled buttons and `aria-live="polite"` feedback creates a significantly more accessible and pleasant UX during data fetching.
**Action:** When implementing optimistic UI updates or async system interactions in plain HTML, avoid using blocking alerts. Always visually disable triggering buttons while requests process and append an accessible, transient toast element that's automatically removed, delaying any necessary page reloads to ensure visibility.
