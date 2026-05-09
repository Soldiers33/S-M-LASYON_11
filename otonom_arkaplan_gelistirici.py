import time
import datetime
from simulasyon_11 import Simule3_Lab_V133

def run_background_loop():
    print(f"[{datetime.datetime.now()}] Initializing Autonomous Background Developer (Otonom Arkaplan Geliştirici)...")

    while True:
        print(f"\n[{datetime.datetime.now()}] Starting new simulation execution cycle...")
        try:
            lab = Simule3_Lab_V133()
            lab.run_all()
            print(f"[{datetime.datetime.now()}] Cycle completed successfully.")
        except Exception as e:
            print(f"[{datetime.datetime.now()}] CRITICAL ERROR in simulation loop: {e}")

        print(f"[{datetime.datetime.now()}] Sleeping for 3600 seconds to prevent rate limits...")
        time.sleep(3600)

if __name__ == "__main__":
    run_background_loop()
