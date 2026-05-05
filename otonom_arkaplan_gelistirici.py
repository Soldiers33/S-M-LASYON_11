import time
import sys
import os
import random
from datetime import datetime

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def log(msg, color=Colors.CYAN):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{color}[{timestamp}] {msg}{Colors.ENDC}")
    sys.stdout.flush()

def main():
    log("INITIALIZING AUTONOMOUS BACKGROUND DEVELOPER (YZ OTONOM SİSTEM)", Colors.HEADER)
    log("Loading Core Modules...", Colors.BLUE)

    # Try importing the main orchestrator
    try:
        from simulasyon_11 import Simule3_Lab_V133
        lab = Simule3_Lab_V133()
        log("SIMULE3_LAB_V133 Loaded successfully.", Colors.GREEN)
    except ImportError as e:
        log(f"CRITICAL ERROR: Failed to load simulasyon_11.py. {e}", Colors.FAIL)
        sys.exit(1)

    log("Starting infinite execution loop (BEN YOKKENDE ARKA PLANDA GELİŞTİR)...", Colors.HEADER)

    iteration = 1
    while True:
        try:
            log(f"--- STARTING AUTONOMOUS CYCLE #{iteration} ---", Colors.BOLD)

            # Execute the grand simulation
            lab.run_all()

            log(f"--- CYCLE #{iteration} COMPLETE ---", Colors.GREEN)

            # Wait before next iteration
            sleep_time = random.randint(60, 180) # Sleep 1-3 mins
            log(f"System cooling down. Waiting {sleep_time} seconds before next cycle...", Colors.WARNING)
            time.sleep(sleep_time)

            iteration += 1

        except Exception as e:
            log(f"Exception during cycle execution: {e}", Colors.FAIL)
            log("Attempting recovery in 30 seconds...", Colors.WARNING)
            time.sleep(30)

if __name__ == "__main__":
    main()
