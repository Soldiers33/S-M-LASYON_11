import time
import os
import sys
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

def run_simulation():
    print(f"\n{Colors.CYAN}[AUTO-RUNNER] Starting Simulation 11 Execution...{Colors.ENDC}")
    try:
        # Run the main simulation process
        subprocess.run(["python3", "simulasyon_11.py"], check=True)
        print(f"{Colors.GREEN}[AUTO-RUNNER] Simulation Executed Successfully.{Colors.ENDC}")
    except subprocess.CalledProcessError as e:
        print(f"{Colors.FAIL}[AUTO-RUNNER] Simulation failed with error code {e.returncode}{Colors.ENDC}")

def run_background_loop():
    print(f"{Colors.BOLD}{Colors.HEADER}=== INITIATING AUTONOMOUS BACKGROUND DEVELOPMENT LOOP ==={Colors.ENDC}")
    print(f"{Colors.WARNING}This process will run indefinitely, querying live APIs and processing the 11-dimensional simulation.{Colors.ENDC}")

    iteration = 1
    while True:
        print(f"\n{Colors.BOLD}{Colors.BLUE}[--- ITERATION {iteration} ---]{Colors.ENDC}")

        # Execute the primary simulation which now includes NASA, Deep Research, and Validation
        run_simulation()

        print(f"{Colors.CYAN}[AUTO-RUNNER] Iteration {iteration} complete. Entering resting cycle.{Colors.ENDC}")
        iteration += 1

        # Use a significant sleep to prevent API rate limiting from NASA/arXiv (e.g. 1 hour)
        # For testing, we use 3600 seconds, but in immediate dev it can be shorter.
        # We'll use 3600 per memory guidelines.
        time.sleep(3600)

if __name__ == "__main__":
    try:
        run_background_loop()
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}[AUTO-RUNNER] Manual termination received. Shutting down autonomous background loop.{Colors.ENDC}")
        sys.exit(0)
