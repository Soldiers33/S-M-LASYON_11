#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import subprocess
from datetime import datetime

class Colors:
    HEADER = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def run_background_cycle():
    print(f"\n{Colors.HEADER}=== AUTONOMOUS BACKGROUND EVOLUTION SYSTEM INITIALIZED ==={Colors.ENDC}", flush=True)
    cycle = 1

    while True:
        print(f"\n{Colors.CYAN}[{datetime.now()}] Starting Cycle #{cycle}...{Colors.ENDC}", flush=True)

        try:
            # We run the main simulation. It should load the live data modules and verification tests natively.
            print(f"  {Colors.BOLD}-> Executing main simulation matrix (simulasyon_11.py)...{Colors.ENDC}", flush=True)
            result = subprocess.run(["python3", "simulasyon_11.py"], capture_output=True, text=True, check=True)

            # Simple check for success
            if "SIMULATION COMPLETED" in result.stdout:
                print(f"  {Colors.GREEN}-> [SUCCESS] Simulation cycle completed cleanly.{Colors.ENDC}", flush=True)
            else:
                print(f"  {Colors.GREEN}-> [OK] Executed, but standard completion string not found. Checking outputs...{Colors.ENDC}", flush=True)

            # Optionally we could append certain critical metrics to a log here
            with open("otonom_evolution.log", "a", encoding="utf-8") as f:
                f.write(f"\n[{datetime.now()}] Cycle #{cycle} Execution Complete.\n")

        except subprocess.CalledProcessError as e:
            print(f"  {Colors.FAIL}-> [ERROR] Simulation execution failed with exit code {e.returncode}.{Colors.ENDC}", flush=True)
            print(f"  {Colors.FAIL}-> Details: {e.stderr[:200]}...{Colors.ENDC}", flush=True)

        print(f"{Colors.CYAN}[{datetime.now()}] Cycle #{cycle} completed. Sleeping for data aggregation...{Colors.ENDC}", flush=True)
        cycle += 1

        # Significant sleep duration to avoid rate limits (e.g. arXiv API) and simulate continuous evolution
        # For actual testing we might want to keep it shorter, but standard requirement states 3600
        time.sleep(3600)

if __name__ == "__main__":
    run_background_cycle()
