import time
import subprocess
from datetime import datetime

class Colors:
    HEADER = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def run_background_loop():
    print(f"{Colors.HEADER}{Colors.BOLD}=== AUTONOMOUS BACKGROUND DEVELOPER & EXECUTOR ==={Colors.ENDC}")
    print(f"{Colors.CYAN}Starting continuous execution and integration loop...{Colors.ENDC}")

    iteration = 1
    try:
        while True:
            print(f"\n{Colors.GREEN}[Iteration {iteration} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]{Colors.ENDC}")
            print(f"{Colors.CYAN}[*] Running Master Simulation...{Colors.ENDC}")

            # Execute the simulation, redirect output to prevent terminal spam
            # but allow capturing success
            result_sim = subprocess.run(['python3', 'simulasyon_11.py'], capture_output=True, text=True)

            if result_sim.returncode == 0:
                print(f"{Colors.GREEN}[+] Simulation ran successfully. Appending log.{Colors.ENDC}")
                with open("autonomous_run.log", "a") as f:
                    f.write(f"[{datetime.now().isoformat()}] Simulation OK\n")
            else:
                print(f"{Colors.HEADER}[!] Simulation Warning: Code non-zero.{Colors.ENDC}")
                with open("autonomous_error.log", "a") as f:
                    f.write(f"[{datetime.now().isoformat()}] Error:\n{result_sim.stderr}\n")

            print(f"{Colors.CYAN}[*] Running Levhi Mahfuz Integrations...{Colors.ENDC}")
            result_levhi = subprocess.run(['python3', 'levhi_mahfuz.py'], capture_output=True, text=True)

            if result_levhi.returncode == 0:
                print(f"{Colors.GREEN}[+] Levhi Mahfuz ran successfully.{Colors.ENDC}")

            print(f"{Colors.CYAN}[*] Sleeping for autonomous development cycle (600s)...{Colors.ENDC}")
            time.sleep(600)  # Sleep 10 minutes between iterations
            iteration += 1

    except KeyboardInterrupt:
        print(f"\n{Colors.HEADER}Autonomous loop terminated gracefully.{Colors.ENDC}")

if __name__ == "__main__":
    run_background_loop()
