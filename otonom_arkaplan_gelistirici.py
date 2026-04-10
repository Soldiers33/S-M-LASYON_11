import time
import subprocess
import datetime
import sys

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    GOLD = '\033[33m'

def run_background_loop(interval_seconds=3600):
    """
    Runs the main simulation (simulasyon_11.py) in a continuous autonomous loop.
    Simulates the 'BEN YOKKENDE ARKA PLANDA GELİŞTİR' requirement.
    """
    print(f"{Colors.HEADER}{Colors.BOLD}=== AUTONOMOUS BACKGROUND SIMULATION LOOP INITIATED ==={Colors.ENDC}")
    print(f"Interval: {interval_seconds} seconds")

    cycle_count = 1

    try:
        while True:
            current_time = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
            print(f"\n{Colors.CYAN}[CYCLE {cycle_count}] Starting execution at {current_time}{Colors.ENDC}")
            print("-" * 60)

            # Execute main simulation script
            try:
                result = subprocess.run(
                    [sys.executable, "simulasyon_11.py"],
                    capture_output=True,
                    text=True
                )

                # Check for execution success
                if result.returncode == 0:
                    print(f"{Colors.GREEN}[CYCLE {cycle_count}] Execution successful.{Colors.ENDC}")
                    # Log a brief snippet of output as confirmation
                    output_snippet = "\n".join(result.stdout.split('\n')[-5:])
                    print(f"Snippet:\n{output_snippet}")
                else:
                    print(f"{Colors.FAIL}[CYCLE {cycle_count}] Execution failed with return code {result.returncode}{Colors.ENDC}")
                    print(f"Error:\n{result.stderr}")

            except Exception as e:
                 print(f"{Colors.FAIL}[CYCLE {cycle_count}] Execution error: {e}{Colors.ENDC}")

            print("-" * 60)
            print(f"{Colors.GOLD}Entering sleep mode for {interval_seconds} seconds...{Colors.ENDC}")

            # Use smaller sleep intervals to allow keyboard interruption
            for _ in range(interval_seconds):
                time.sleep(1)

            cycle_count += 1

    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}Autonomous background loop terminated by user.{Colors.ENDC}")

if __name__ == "__main__":
    # For testing purposes, we can run a short cycle if desired,
    # but the default simulates the long-running background process.
    # We will use a default of 10 seconds for initial testing.
    run_background_loop(interval_seconds=10)
