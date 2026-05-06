import time
import sys
from simulasyon_11 import Simule3_Lab_V133, Colors

def main():
    print(f"{Colors.BOLD}{Colors.GOLD}--- AUTONOMOUS BACKGROUND DEVELOPER ACTIVATED ---{Colors.ENDC}")
    print(f"{Colors.CYAN}The simulation will now run continuously in the background, executing all modules...{Colors.ENDC}")

    iteration = 1
    try:
        while True:
            print(f"\n{Colors.BOLD}{Colors.PURPLE}=== ITERATION {iteration} ==={Colors.ENDC}")
            lab = Simule3_Lab_V133()
            lab.run_all()
            print(f"{Colors.GREEN}[ITERATION {iteration} COMPLETED. WAITING FOR NEXT CYCLE...]{Colors.ENDC}")
            iteration += 1
            time.sleep(10) # Wait 10 seconds between iterations to avoid spamming the console too fast
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}Autonomous execution terminated by user.{Colors.ENDC}")
        sys.exit(0)

if __name__ == "__main__":
    main()
