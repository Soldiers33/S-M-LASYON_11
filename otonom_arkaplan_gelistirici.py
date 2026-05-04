import time
import sys
import datetime

# Attempt to import main loop. We'll use try-except to avoid issues if it doesn't exist yet.
try:
    from simulasyon_11 import Simule3_Lab_V133
except ImportError:
    Simule3_Lab_V133 = None

def run_background_loop():
    print(f"Starting Autonomous Background Simulator at {datetime.datetime.now()}")
    iteration = 1

    while True:
        print(f"\n--- BACKGROUND ITERATION {iteration} ---")
        if Simule3_Lab_V133:
            try:
                lab = Simule3_Lab_V133()
                lab.run_all()
            except Exception as e:
                print(f"Simulation Error: {e}")
        else:
            print("Simule3_Lab_V133 not found.")

        print("Sleeping for 10 seconds before next iteration (to prevent sandbox lock)...")
        time.sleep(10)
        iteration += 1

if __name__ == "__main__":
    run_background_loop()
