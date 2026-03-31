with open('uv_monte_carlo_runner.py', 'r') as f:
    content = f.read()

# Replace all "\r\033[K  Simulating..." to fix the extra "Simulating..." print
content = content.replace(
    "\\r\\033[K  Simulating...",
    "\\r\\033[K    Progress:"
)

with open('uv_monte_carlo_runner.py', 'w') as f:
    f.write(content)
