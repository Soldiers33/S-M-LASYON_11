import time
import subprocess
from datetime import datetime
import sys

def background_loop():
    print("--- AUTONOMOUS BACKGROUND DEVELOPER SIMULATION INITIATED ---")
    print(f"[{datetime.now()}] Background process started.")

    cycle = 1
    # User strictly mandates a continuous infinite background run
    while True:
        print(f"\n[{datetime.now()}] --- EXECUTING GRAND SIMULATION CYCLE {cycle} ---")
        try:
            # Execute the main simulation via shell to cleanly isolate its execution
            result = subprocess.run(["python3", "simulasyon_11.py"], capture_output=True, text=True)
            print("[+] Simulation cycle finished.")
            # Log output to a file without checking it into version control
            with open("run_output.txt", "a") as f:
                f.write(f"\n--- CYCLE {cycle} AT {datetime.now()} ---\n")
                f.write(result.stdout)
                if result.stderr:
                    f.write("\n[ERRORS]\n")
                    f.write(result.stderr)
        except Exception as e:
            print(f"[-] Critical Error in autonomous loop: {e}")

        cycle += 1
        # Sleep for a significant amount of time before the next iteration
        # 3600 seconds = 1 hour loop to prevent API rate limiting.
        print(f"[{datetime.now()}] Sleeping before next quantum processing cycle...")
        time.sleep(3600)

if __name__ == "__main__":
    background_loop()
