## 2024-03-02 - Inline Terminal Loading Bars
**Learning:** Terminal output can get cluttered with successive `print()` statements for loading steps. Using `sys.stdout.write` in combination with the carriage return character (`\r`) allows for updating the same line in place.
**Action:** Use `sys.stdout.write` and `\r` for terminal progress/loading indicators to improve CLI UX.
