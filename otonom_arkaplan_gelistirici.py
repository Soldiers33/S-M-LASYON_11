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

def print_log(msg):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] {msg}")

def run_simulation():
    try:
        print_log(f"{Colors.CYAN}Starting autonomous execution of Master Simulation (simulasyon_11.py)...{Colors.ENDC}")
        result = subprocess.run(["python3", "simulasyon_11.py"], capture_output=True, text=True)
        if result.returncode == 0:
            print_log(f"{Colors.GREEN}Simulation executed successfully.{Colors.ENDC}")
            # Optionally log output to file
            with open("otonom_run.log", "a") as f:
                f.write(f"\n--- RUN AT {datetime.datetime.now()} ---\n")
                f.write(result.stdout[:1000] + "\n...[truncated]...\n")
        else:
            print_log(f"{Colors.FAIL}Simulation failed with return code {result.returncode}.{Colors.ENDC}")
            print_log(result.stderr)
    except Exception as e:
        print_log(f"{Colors.FAIL}Error running simulation: {e}{Colors.ENDC}")

def continuous_background_loop():
    print_log(f"{Colors.HEADER}=== OTONOM ARKA PLAN GELISTIRICI INITIATED ==={Colors.ENDC}")
    print_log("Continuous autonomous loop active. Will run simulation and fetch external data periodically.")

    while True:
        run_simulation()

        # We enforce a significant sleep (e.g., 3600 seconds = 1 hour) to prevent API rate limiting.
        sleep_duration = 3600
        print_log(f"{Colors.WARNING}Cycle complete. Sleeping for {sleep_duration} seconds...{Colors.ENDC}")
        time.sleep(sleep_duration)

if __name__ == "__main__":
    continuous_background_loop()
