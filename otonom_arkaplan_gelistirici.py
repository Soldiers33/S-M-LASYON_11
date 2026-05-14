import time
import subprocess
import os

class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def run_simulation():
    try:
        print(f"\n{Colors.BOLD}{Colors.CYAN}[{time.strftime('%Y-%m-%d %H:%M:%S')}] Launching Master Simulation (simulasyon_11.py)...{Colors.ENDC}")
        # Run the main simulation script
        result = subprocess.run(["python3", "simulasyon_11.py"], capture_output=True, text=True)

        if result.returncode == 0:
            print(f"{Colors.GREEN}[OK] Simulation executed successfully.{Colors.ENDC}")
            # Optionally log output to a file to prevent console spam
            with open("arkaplan_simulasyon_log.txt", "a") as f:
                f.write(f"\n--- RUN: {time.strftime('%Y-%m-%d %H:%M:%S')} ---\n")
                # write tail of result
                f.write(result.stdout[-1000:])
        else:
            print(f"{Colors.WARNING}[WARNING] Simulation exited with code {result.returncode}.{Colors.ENDC}")
            with open("arkaplan_simulasyon_error.log", "a") as f:
                f.write(f"\n--- ERROR: {time.strftime('%Y-%m-%d %H:%M:%S')} ---\n")
                f.write(result.stderr)

    except Exception as e:
        print(f"{Colors.WARNING}[ERROR] Failed to run simulation: {e}{Colors.ENDC}")

def autonomous_loop():
    print(f"{Colors.BOLD}{Colors.GREEN}Autonomous Background Developer Started.{Colors.ENDC}")
    print("This script will run indefinitely, periodically executing and expanding the simulation.")
    print("Press Ctrl+C to terminate.")

    iteration = 1
    while True:
        print(f"\n--- Iteration {iteration} ---")
        run_simulation()

        # Continuous background sleep. 3600 seconds = 1 hour.
        sleep_time = 3600
        print(f"Sleeping for {sleep_time} seconds before next run...")
        time.sleep(sleep_time)
        iteration += 1

if __name__ == "__main__":
    autonomous_loop()
