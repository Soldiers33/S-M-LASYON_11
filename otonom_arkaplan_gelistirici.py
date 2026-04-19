import time
import datetime
from simulasyon_11 import Simule3_Lab_V133

def run_background_loop():
    print("\033[96m" + "="*60)
    print("AUTONOMOUS BACKGROUND SIMULATION LOOP INITIATED")
    print("Monitoring and compiling 11-dimensional data indefinitely...")
    print("="*60 + "\033[0m\n")

    iteration = 1
    while True:
        try:
            print(f"\n\033[93m[ITERATION {iteration}] - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\033[0m")
            lab = Simule3_Lab_V133()
            lab.run_all()

            print(f"\n\033[92mIteration {iteration} complete. System resting before next cycle...\033[0m")
            # Sleep for a period before running the next full simulation loop
            time.sleep(10)
            iteration += 1

        except Exception as e:
            print(f"\033[91m[!] CRITICAL ERROR in autonomous loop: {e}\033[0m")
            print("Attempting to restart cycle in 30 seconds...")
            time.sleep(30)

if __name__ == "__main__":
    run_background_loop()
