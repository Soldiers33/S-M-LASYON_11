import time
import subprocess
from datetime import datetime

def run_background_loop():
    print(f"[{datetime.now()}] Otonom Arkaplan Geliştirici Started.")
    print("Initiating infinite background simulation loop...")

    while True:
        try:
            print(f"\n[{datetime.now()}] Executing master simulation...")
            # Run the main simulation
            subprocess.run(["python3", "simulasyon_11.py"], check=True)
            print(f"[{datetime.now()}] Simulation execution completed.")
        except subprocess.CalledProcessError as e:
            print(f"[{datetime.now()}] Error executing simulation: {e}")
        except Exception as e:
             print(f"[{datetime.now()}] Unexpected Error: {e}")

        # Sleep for 1 hour to prevent API rate limiting
        sleep_duration = 3600
        print(f"[{datetime.now()}] Sleeping for {sleep_duration} seconds...")
        time.sleep(sleep_duration)

if __name__ == '__main__':
    run_background_loop()
