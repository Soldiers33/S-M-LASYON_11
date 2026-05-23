import time
import datetime
import subprocess
import sys
import os

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

def write_log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_msg = f"[{timestamp}] {message}"
    print(log_msg, flush=True)
    with open("otonom_arkaplan.log", "a") as f:
        f.write(log_msg + "\n")

def main():
    write_log(f"{Colors.BOLD}{Colors.GREEN}=== OTONOM ARKA PLAN GELİŞTİRİCİ BAŞLATILDI ==={Colors.ENDC}")
    write_log("Background execution loop initiated. Will run continuous autonomous updates.")

    iteration = 1
    while True:
        write_log(f"\n{Colors.CYAN}--- DÖNGÜ ITERASYONU: {iteration} ---{Colors.ENDC}")

        # 1. Run NASA Live Data Module
        write_log("Çalıştırılıyor: NASA Veri Çekici (modul_nasa_live_data.py)...")
        try:
            subprocess.run([sys.executable, "modul_nasa_live_data.py"], check=True, capture_output=True, text=True)
            write_log("NASA verisi başarıyla senkronize edildi.")
        except subprocess.CalledProcessError as e:
            write_log(f"{Colors.FAIL}Hata: NASA Veri Modülü Çöktü: {e}{Colors.ENDC}")

        # 2. Run Deep Research Module
        write_log("Çalıştırılıyor: Derin Araştırma Modülü (deep_research_module.py)...")
        try:
            subprocess.run([sys.executable, "deep_research_module.py"], check=True, capture_output=True, text=True)
            write_log("Derin araştırma başarıyla tamamlandı ve sentez verileri çıkarıldı.")
        except subprocess.CalledProcessError as e:
             write_log(f"{Colors.FAIL}Hata: Derin Araştırma Modülü Çöktü: {e}{Colors.ENDC}")

        # 3. Run Main Simulation Orchestrator (simulasyon_11.py)
        # Note: We just execute a dry run of the main script to ensure it validates the integration
        write_log("Çalıştırılıyor: Ana Simülasyon Motoru (simulasyon_11.py)...")
        try:
            # We use capture_output so we don't flood the terminal infinitely but can log the success.
            subprocess.run([sys.executable, "simulasyon_11.py"], check=True, capture_output=True, text=True)
            write_log(f"{Colors.BOLD}{Colors.GREEN}Simülasyon_11 Başarıyla Tamamlandı ve SENTEZ-7 İşlendi.{Colors.ENDC}")
        except subprocess.CalledProcessError as e:
            write_log(f"{Colors.FAIL}Kritik Hata: Simülasyon_11 Motoru Çöktü! {e}{Colors.ENDC}")

        iteration += 1
        write_log(f"{Colors.WARNING}Sistem API Rate Limitlerine (NASA/arXiv) Takılmamak için 3600 Saniye Uyku Moduna Geçiyor...{Colors.ENDC}")
        time.sleep(3600)  # Sleep for 1 hour to prevent API rate limiting from external sources.

if __name__ == "__main__":
    main()
