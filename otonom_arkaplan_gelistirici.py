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


def run_background_loop():
    print(f"{Colors.BOLD}{Colors.HEADER}================================================={Colors.ENDC}", flush=True)
    print(f"{Colors.BOLD}{Colors.HEADER}[AUTONOMOUS] Starting Infinite Background Development Loop{Colors.ENDC}", flush=True)
    print(f"{Colors.BOLD}{Colors.HEADER}================================================={Colors.ENDC}", flush=True)

    iteration = 1
    while True:
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"\n{Colors.CYAN}[Iteration {iteration}] Time: {current_time}{Colors.ENDC}", flush=True)
        print(f"{Colors.MAGENTA}>>> Executing main simulation to aggregate newest findings...{Colors.ENDC}", flush=True)

        try:
            # We run the main simulation file. If we run it as subprocess, we capture the stdout if needed or just let it print.
            # In our case we let it output directly.
            subprocess.run(["python3", "simulasyon_11.py"], check=True)
            print(f"{Colors.GREEN}>>> Simulation cycle completed successfully.{Colors.ENDC}", flush=True)
        except subprocess.CalledProcessError as e:
            print(f"{Colors.FAIL}>>> Simulation cycle encountered an error: {e}{Colors.ENDC}", flush=True)

        print(f"{Colors.GOLD}>>> Sleeping for 3600 seconds to respect API rate limits...{Colors.ENDC}", flush=True)
        time.sleep(3600)
        iteration += 1

if __name__ == "__main__":
    run_background_loop()
