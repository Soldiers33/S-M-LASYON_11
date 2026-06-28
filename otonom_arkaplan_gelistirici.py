#!/usr/bin/env python3
import time
import subprocess
import datetime
import sys

def run_background_process():
    print(f"[{datetime.datetime.now()}] Starting autonomous background developer...", flush=True)
    scripts_to_run = [
        "simulasyon_11.py",
        "levhi_mahfuz.py",
        "verify_constants.py"
    ]

    cycle_count = 0
    while True:
        cycle_count += 1
        print(f"\\n[{datetime.datetime.now()}] --- CYCLE {cycle_count} ---", flush=True)

        for script in scripts_to_run:
            print(f"[{datetime.datetime.now()}] Running {script}...", flush=True)
            try:
                result = subprocess.run(["python3", script], check=True, capture_output=True, text=True)
                print(f"[{datetime.datetime.now()}] {script} executed successfully.", flush=True)
            except subprocess.CalledProcessError as e:
                print(f"[{datetime.datetime.now()}] ERROR running {script}: {e.stderr}", file=sys.stderr, flush=True)
            except Exception as e:
                print(f"[{datetime.datetime.now()}] UNEXPECTED ERROR with {script}: {e}", file=sys.stderr, flush=True)

        print(f"[{datetime.datetime.now()}] Cycle complete. Sleeping for 10 seconds...", flush=True)
        # Sleep for a short duration to demonstrate the loop without taking forever
        time.sleep(10)

if __name__ == "__main__":
    run_background_process()
