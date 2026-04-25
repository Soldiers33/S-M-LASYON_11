import time
from simulasyon_11 import Simule3_Lab_V133, Colors

def otonom_dongu():
    print(f"{Colors.BOLD}{Colors.GOLD}*** STARTING AUTONOMOUS BACKGROUND DEVELOPMENT LOOP ***{Colors.ENDC}")
    lab = Simule3_Lab_V133()
    iteration = 1

    while True:
        print(f"\n{Colors.BOLD}{Colors.CYAN}--- AUTONOMOUS ITERATION {iteration} ---{Colors.ENDC}")
        lab.run_all()
        print(f"\n{Colors.GREEN}[+] Iteration {iteration} completed. Waiting for next cycle...{Colors.ENDC}")

        # Add a sleep to prevent rapid infinite looping that could freeze the terminal,
        # but keep it continuous per user directive.
        time.sleep(30)
        iteration += 1

if __name__ == "__main__":
    otonom_dongu()
