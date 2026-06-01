import time
import subprocess
import sys
from datetime import datetime

def run_background_loop():
    print(f"[{datetime.now()}] Autonomous Background Developer Module Started.", flush=True)

    while True:
        print(f"\n[{datetime.now()}] --- Initiating Autonomous Cycle ---", flush=True)

        # Execute the main simulation which now includes SENTEZ-7, NASA, and Deep Research
        try:
            print("Executing simulasyon_11.py...", flush=True)
            result = subprocess.run([sys.executable, "simulasyon_11.py"], check=True, capture_output=True, text=True)
            # Just print the last 10 lines to keep the log manageable
            lines = result.stdout.split('\n')
            for line in lines[-15:]:
                if line.strip():
                    print(f"SIM OUTPUT: {line}", flush=True)
            print(f"[{datetime.now()}] Simulation cycle completed successfully.", flush=True)
        except subprocess.CalledProcessError as e:
            print(f"[{datetime.now()}] Error running simulation: {e}", flush=True)
            if e.stdout:
                print(f"STDOUT: {e.stdout}", flush=True)
            if e.stderr:
                print(f"STDERR: {e.stderr}", flush=True)

        print(f"[{datetime.now()}] Cycle finished. Sleeping for 3600 seconds to prevent API rate limiting...", flush=True)
        time.sleep(3600)

if __name__ == "__main__":
    run_background_loop()
