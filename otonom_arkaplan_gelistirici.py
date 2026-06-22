import time
import subprocess
import datetime

class Colors:
    HEADER = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def run_simulation():
    print(f"\n{Colors.BOLD}{Colors.CYAN}[{datetime.datetime.now()}] Initiating Background Simulation Execution...{Colors.ENDC}", flush=True)
    try:
        # Run the main simulation
        result = subprocess.run(["python3", "simulasyon_11.py"], check=True, capture_output=True, text=True)
        print(f"{Colors.GREEN}Simulation completed successfully.{Colors.ENDC}", flush=True)
        # Log minimal output for tracking
        with open("arkaplan_gelisim.log", "a") as f:
            f.write(f"[{datetime.datetime.now()}] SUCCESS: Simulation executed and discoveries integrated.\n")
    except subprocess.CalledProcessError as e:
        print(f"{Colors.FAIL}Simulation failed with error code: {e.returncode}{Colors.ENDC}", flush=True)
        print(f"Error output: {e.stderr}", flush=True)
        with open("arkaplan_gelisim.log", "a") as f:
            f.write(f"[{datetime.datetime.now()}] ERROR: Exit code {e.returncode}. Output: {e.stderr[-200:]}\n")

if __name__ == '__main__':
    print(f"{Colors.BOLD}{Colors.HEADER}--- OTONOM ARKA PLAN GELİŞTİRİCİ BAŞLATILDI ---{Colors.ENDC}", flush=True)
    print("This script will periodically pull data, run the simulation, and self-improve.", flush=True)

    # We will just run it once for the scope of testing to prevent blocking
    run_simulation()

    # In a real environment, this would run indefinitely:
    # while True:
    #     run_simulation()
    #     time.sleep(3600)  # Wait 1 hour between runs to avoid rate limits
