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

## 2026-04-01 - Monte Carlo CLI Loading Experience
**Learning:** When implementing in-place CLI loading feedback for long-running processes (e.g., iterations in Monte Carlo simulations), the initial 'loading' feedback must be printed before the iteration loop starts, and the final 'success/OK' indicator must be printed only after the loop fully completes. Otherwise, it creates a falsely reassuring user experience or causes subsequent multi-line text to overlap. Also, `loading_bar` in Python prints its own newline by default, so we do not need to add `\n` and use `end=''`.
**Action:** Updated `kar_topu_v5_v3_synthesis.py`'s `monte_carlo_phase3_stability` method to display initial 'Loading...', iterate in-place using `\r\033[K`, and then finalize with a distinct `[OK] Simulation Complete` message after the loop concludes. Fixed `simulasyon_11.py`'s `loading_bar` to rely on Python's default newline behavior.
