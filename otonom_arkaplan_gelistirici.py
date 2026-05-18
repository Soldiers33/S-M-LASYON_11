import time
import subprocess
import datetime

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    GOLD = '\033[33m'
    MAGENTA = '\033[35m'
    PURPLE = '\033[35m'

print(f"{Colors.BOLD}{Colors.PURPLE}[AUTONOMOUS ORCHESTRATOR] STARTING CONTINUOUS BACKGROUND EXECUTION...{Colors.ENDC}")

iteration = 0
while True:
    iteration += 1
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{Colors.BOLD}{Colors.CYAN}--- ITERATION {iteration} | TIME: {current_time} ---{Colors.ENDC}")

    try:
        print(f"{Colors.GREEN}Executing Master Simulation...{Colors.ENDC}")
        subprocess.run(["python3", "simulasyon_11.py"], check=True)

        print(f"{Colors.GREEN}Executing Validation Core...{Colors.ENDC}")
        subprocess.run(["python3", "levhi_mahfuz.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"{Colors.FAIL}⚠ Execution Error during Iteration {iteration}: {e}{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.FAIL}⚠ Unexpected Error: {e}{Colors.ENDC}")

    print(f"{Colors.BOLD}{Colors.GOLD}Iteration {iteration} Complete. Entering Hyper-Sleep Mode to preserve API rates.{Colors.ENDC}")

    # 1 Hour Sleep Loop to prevent API rate limit and resource exhaustion
    time.sleep(3600)
