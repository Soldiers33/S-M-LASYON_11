import time
import os
import sys

# Import the main simulation kernel
try:
    from simulasyon_11 import Simule3_Lab_V133
except ImportError:
    print("Error: Could not import Simule3_Lab_V133 from simulasyon_11.py")
    sys.exit(1)

def run_background_loop():
    print("Starting Autonomous Background Execution Loop...")
    iteration = 1
    while True:
        print(f"\n[{time.strftime('%Y-%m-%d %H:%M:%S')}] --- BACKGROUND ITERATION {iteration} ---")

        # Instantiate and run the main simulation
        try:
            lab = Simule3_Lab_V133()
            lab.run_all()
        except Exception as e:
            print(f"Error during simulation execution: {e}")

        print(f"Iteration {iteration} complete. Sleeping for next cycle...")
        # Sleep for a significant duration (e.g., 3600 seconds = 1 hour) to avoid API rate limits
        # However, for testing purposes, we'll keep it relatively short but not too short
        time.sleep(60)
        iteration += 1

if __name__ == "__main__":
    run_background_loop()
