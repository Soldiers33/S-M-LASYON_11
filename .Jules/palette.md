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

## 2026-03-31 - [CLI Progress Tracking Pattern]
**Learning:** Adding `print('\r\033[K Progress...', end='', flush=True)` correctly updates the terminal in place for long-running iterative calculations (like Monte Carlo simulations). However, you must pair it with a starting `print('  Simulating...', end='', flush=True)` before the loop, and an empty `print()` *after* the loop to ensure clean transition to the next terminal output without overlap.
**Action:** Applied to `uv_monte_carlo_runner.py`'s 4 main loops to prevent the CLI from appearing "frozen" during 100k iteration tests.
