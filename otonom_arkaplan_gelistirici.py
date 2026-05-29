import time
import datetime
import subprocess

def run_simulation():
    print(f"\n[{datetime.datetime.now()}] Starting autonomous cycle...", flush=True)
    try:
        # We run the main simulation directly via subprocess
        # This prevents module state leak and safely executes the whole orchestrator.
        print("[AUTONOMOUS] Calling simulasyon_11.py...", flush=True)
        result = subprocess.run(["python3", "simulasyon_11.py"], capture_output=True, text=True)

        if result.returncode == 0:
            print("[AUTONOMOUS] Simulation cycle completed successfully.", flush=True)
            # You could parse result.stdout here if needed
        else:
            print(f"[AUTONOMOUS] Simulation encountered an error: {result.stderr}", flush=True)

    except Exception as e:
        print(f"[AUTONOMOUS] Exception during execution: {str(e)}", flush=True)

if __name__ == "__main__":
    print("--- AUTONOMOUS BACKGROUND SIMULATION DEVELOPER ACTIVE ---", flush=True)
    while True:
        run_simulation()

        # Sleep for a long period to prevent rate limiting from NASA/arXiv APIs
        # Per memory guidelines, use a large sleep like 3600 seconds (1 hour).
        sleep_time = 3600
        print(f"[{datetime.datetime.now()}] Cycle finished. Sleeping for {sleep_time} seconds...", flush=True)
        time.sleep(sleep_time)
