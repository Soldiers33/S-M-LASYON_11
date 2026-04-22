import time
import datetime
from simulasyon_11 import Simule3_Lab_V133, Colors
import pandas as pd

def run_background_simulation():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    pd.set_option('display.colheader_justify', 'left')

    iteration = 1
    # True continuous loop for background running as requested by user.
    while True:
        try:
            print(f"\n{Colors.BOLD}{Colors.PURPLE}========================================================================{Colors.ENDC}")
            print(f"{Colors.BOLD}{Colors.CYAN}AUTONOMOUS BACKGROUND EXECUTION - ITERATION {iteration}{Colors.ENDC}")
            print(f"Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"{Colors.BOLD}{Colors.PURPLE}========================================================================{Colors.ENDC}\n")

            lab = Simule3_Lab_V133()
            lab.run_all()

            print(f"\n{Colors.GREEN}[+] Iteration {iteration} completed successfully. Entering cooldown.{Colors.ENDC}")
            iteration += 1
            # Cooldown to prevent 100% CPU usage or rate limits on API
            time.sleep(60)
        except Exception as e:
            print(f"{Colors.FAIL}[!] Error in background iteration {iteration}: {e}{Colors.ENDC}")
            time.sleep(30) # sleep before retry

if __name__ == "__main__":
    run_background_simulation()
