import time
from simulasyon_11 import Simule3_Lab_V133, Colors

def run_background_loop():
    print(f"{Colors.HEADER}Starting Autonomous Background Developer Loop...{Colors.ENDC}")
    iteration = 1
    while True:
        print(f"\n{Colors.WARNING}--- ITERATION {iteration} ---{Colors.ENDC}")
        try:
            lab = Simule3_Lab_V133()
            lab.run_all()
            print(f"{Colors.GREEN}Iteration {iteration} complete. Sleeping...{Colors.ENDC}")
        except Exception as e:
            print(f"{Colors.FAIL}Error during iteration {iteration}: {e}{Colors.ENDC}")

        # Sleep to simulate background delay and prevent CPU thrashing
        time.sleep(5)
        iteration += 1

if __name__ == "__main__":
    run_background_loop()
