with open('uv_monte_carlo_runner.py', 'r') as f:
    content = f.read()

# Replace all occurrences of "for _ in range(self.iterations):"
content = content.replace(
    "for _ in range(self.iterations):",
    """print("  Simulating...", end='', flush=True)
        for i in range(self.iterations):"""
)

with open('uv_monte_carlo_runner.py', 'w') as f:
    f.write(content)
