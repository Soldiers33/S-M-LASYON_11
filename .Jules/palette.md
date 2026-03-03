## 2026-03-03 - [Inline CLI Progress indicators]
**Learning:** When implementing command-line loading states or progress indicators, printing multiple newlines causes terminal clutter. Using print with end="" and flush=True along with carriage returns (\r) allows updating the same line, resulting in a cleaner and more professional user experience.
**Action:** Default to using carriage returns (\r) for CLI loading bars and dynamic progress messages instead of new print statements.
