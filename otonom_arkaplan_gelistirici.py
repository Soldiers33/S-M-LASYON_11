import sys
import time
import datetime
import subprocess

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    MAGENTA = '\033[35m'
    GOLD = '\033[33m'

def log_to_knowledge_base(data_str):
    with open("AI_KNOWLEDGE_BASE_11.md", "a", encoding="utf-8") as f:
        f.write(f"\n\n### Autonomous Update: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(data_str)

def main():
    print(f"{Colors.BOLD}{Colors.MAGENTA}STARTING AUTONOMOUS BACKGROUND EXECUTOR...{Colors.ENDC}", flush=True)

    iteration = 0
    while True:
        iteration += 1
        print(f"\n{Colors.CYAN}--- Background Iteration {iteration} at {datetime.datetime.now()} ---{Colors.ENDC}", flush=True)

        try:
            # Run the main simulation and capture output
            print(f"{Colors.BLUE}Executing simulasyon_11.py...{Colors.ENDC}", flush=True)
            result = subprocess.run([sys.executable, 'simulasyon_11.py'], capture_output=True, text=True, check=True)
            output_snippet = result.stdout[-500:] if len(result.stdout) > 500 else result.stdout

            log_msg = f"**Simulation Status**: SUCCESS\n\n**Output Snippet**:\n```\n{output_snippet}\n```"
            log_to_knowledge_base(log_msg)
            print(f"{Colors.GREEN}Simulation executed and logged successfully.{Colors.ENDC}", flush=True)

        except subprocess.CalledProcessError as e:
            print(f"{Colors.FAIL}Simulation failed with error code {e.returncode}{Colors.ENDC}", flush=True)
            log_to_knowledge_base(f"**Simulation Status**: FAILED (Code {e.returncode})\n\n**Error**:\n```\n{e.stderr}\n```")

        print(f"{Colors.WARNING}Sleeping for 3600 seconds to prevent API limits...{Colors.ENDC}", flush=True)
        # We will use 3600 in real scenario. For quick test, we can just sleep briefly, but memory says "use significant sleep duration like time.sleep(3600) instead of short testing intervals"
        time.sleep(3600)

if __name__ == "__main__":
    main()
