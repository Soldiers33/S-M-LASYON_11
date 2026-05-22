import time
import datetime
import subprocess
import os

class Colors:
    HEADER = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def log(msg):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {msg}", flush=True)

def run_background_loop():
    log(f"{Colors.HEADER}=== AUTONOMOUS BACKGROUND DEVELOPER STARTED ==={Colors.ENDC}")

    cycle_count = 0
    while True:
        cycle_count += 1
        log(f"{Colors.CYAN}--- Cycle {cycle_count} Initiated ---{Colors.ENDC}")

        try:
            # Run the master simulation to ensure all updates, including API fetches,
            # are executed in the background.
            log("Executing simulasyon_11.py...")
            result = subprocess.run(
                ['python3', 'simulasyon_11.py'],
                capture_output=True, text=True, timeout=60
            )

            if result.returncode == 0:
                log(f"{Colors.GREEN}[OK] Simulation executed successfully.{Colors.ENDC}")
            else:
                log(f"{Colors.FAIL}[ERROR] Simulation failed with return code {result.returncode}.{Colors.ENDC}")
                log(f"Error output: {result.stderr}")

        except Exception as e:
            log(f"{Colors.FAIL}[CRITICAL] Error running simulation: {e}{Colors.ENDC}")

        log(f"{Colors.WARNING}Sleeping for 3600 seconds (1 hour) to avoid API rate limits...{Colors.ENDC}")
        time.sleep(3600)

if __name__ == "__main__":
    run_background_loop()