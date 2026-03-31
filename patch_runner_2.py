import re

with open('uv_monte_carlo_runner.py', 'r') as f:
    content = f.read()

# Replace sirius loop end
content = content.replace(
    "            deviation = abs(test_freq - cube_11)\n            deviations.append(deviation)",
    """            deviation = abs(test_freq - cube_11)
            deviations.append(deviation)

            if (i + 1) % (self.iterations // 10) == 0:
                progress = ((i + 1) / self.iterations) * 100
                print(f"\\r\\033[K  Simulating... {progress:5.1f}% ({i+1:,}/{self.iterations:,})", end='', flush=True)
        print()"""
)

# Replace enoch loop end
content = content.replace(
    "            error = abs(test_freq / base_11 - 1.0)\n            errors.append(error)",
    """            error = abs(test_freq / base_11 - 1.0)
            errors.append(error)

            if (i + 1) % (self.iterations // 10) == 0:
                progress = ((i + 1) / self.iterations) * 100
                print(f"\\r\\033[K  Simulating... {progress:5.1f}% ({i+1:,}/{self.iterations:,})", end='', flush=True)
        print()"""
)

# Replace giza loop end
content = content.replace(
    "            precisions.append(precision)",
    """            precisions.append(precision)

            if (i + 1) % (self.iterations // 10) == 0:
                progress = ((i + 1) / self.iterations) * 100
                print(f"\\r\\033[K  Simulating... {progress:5.1f}% ({i+1:,}/{self.iterations:,})", end='', flush=True)
        print()"""
)

# Replace antigravity loop end
content = content.replace(
    "            error = abs(result - formula_target)\n            errors.append(error)",
    """            error = abs(result - formula_target)
            errors.append(error)

            if (i + 1) % (self.iterations // 10) == 0:
                progress = ((i + 1) / self.iterations) * 100
                print(f"\\r\\033[K  Simulating... {progress:5.1f}% ({i+1:,}/{self.iterations:,})", end='', flush=True)
        print()"""
)

with open('uv_monte_carlo_runner.py', 'w') as f:
    f.write(content)
