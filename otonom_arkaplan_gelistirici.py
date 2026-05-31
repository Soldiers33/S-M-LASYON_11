import time
import subprocess
import sys

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    GOLD = '\033[33m'
    MAGENTA = '\033[35m'
    PURPLE = '\033[35m'

def run_simulation_cycle():
    print(f"{Colors.HEADER}--- OTONOM ARKA PLAN GELİŞTİRİCİ DÖNGÜSÜ BAŞLIYOR ---{Colors.ENDC}", flush=True)

    print(f"{Colors.CYAN}1. Running Deep Research...{Colors.ENDC}", flush=True)
    try:
        subprocess.run(["python3", "deep_research_module.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"{Colors.FAIL}Deep Research failed: {e}{Colors.ENDC}", flush=True)

    print(f"{Colors.CYAN}2. Fetching NASA Live Data...{Colors.ENDC}", flush=True)
    try:
        subprocess.run(["python3", "modul_nasa_live_data.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"{Colors.FAIL}NASA Fetch failed: {e}{Colors.ENDC}", flush=True)

    print(f"{Colors.CYAN}3. Running Validation Tests...{Colors.ENDC}", flush=True)
    try:
        subprocess.run(["python3", "dogrulama_testleri.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"{Colors.FAIL}Validation tests failed: {e}{Colors.ENDC}", flush=True)

    print(f"{Colors.CYAN}4. Running Main Simulation (simulasyon_11.py)...{Colors.ENDC}", flush=True)
    try:
        with open("final_simulasyon_output.txt", "w") as f:
            subprocess.run(["python3", "simulasyon_11.py"], stdout=f, stderr=subprocess.STDOUT, check=True)
        print(f"{Colors.GREEN}Main Simulation run successfully. Output saved to final_simulasyon_output.txt.{Colors.ENDC}", flush=True)
    except subprocess.CalledProcessError as e:
        print(f"{Colors.FAIL}Main Simulation failed: {e}{Colors.ENDC}", flush=True)

    print(f"{Colors.GREEN}--- DÖNGÜ TAMAMLANDI. 1 SAAT BEKLENİYOR ---{Colors.ENDC}", flush=True)

if __name__ == "__main__":
    while True:
        run_simulation_cycle()
        time.sleep(3600)
