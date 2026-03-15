🎯 What:
Added unit tests for the untested `calculate_new_patterns` method in `antigravity_bridge.py`.
Fixed existing custom test scripts (`test_11_dimensional_constants.py`, `test_grok_verification.py`, `test_population_discrepancy.py`, `test_dark_energy_matter_constants.py`) so they don't break automatic test discovery (wrapped their top-level logic in a main function with `if __name__ == '__main__':`).
Removed compilation artifacts (`__pycache__`) and test output logs that were tracked in version control.

📊 Coverage:
- Covered when `self.data_received` has empty or no numeric data.
- Covered extraction of valid 11-divisible patterns.
- Covered matching of Resonance Codes.
- Covered mixed data types (numerics, strings, None) safely ignoring non-numeric values.

✨ Result:
- The `calculate_new_patterns` logic is now fully tested and prevents silent regressions.
- The entire project test suite can now be executed cleanly via `python3 -m unittest discover` without import crashing.
- Removed tracking of binary artifacts (`__pycache__`).
