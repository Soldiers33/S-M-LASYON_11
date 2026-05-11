import time
import datetime
import subprocess

class Colors:
    HEADER = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def run_simulation():
    print(f"\n{Colors.BOLD}{Colors.CYAN}--- OTONOM ARKA PLAN GELİŞTİRİCİ BAŞLIYOR ---{Colors.ENDC}")
    print(f"Zaman: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    try:
        # Run the main simulation
        result = subprocess.run(["python3", "simulasyon_11.py"], capture_output=True, text=True)
        print(f"{Colors.GREEN}[+] Simülasyon_11 Başarıyla Çalıştırıldı.{Colors.ENDC}")
        # Optionally, you can write the result output to a continuous log file
        with open("otonom_calisma_kaydi.log", "a") as log_file:
            log_file.write(f"\n\n--- ÇALIŞTIRMA ZAMANI: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
            log_file.write(result.stdout)
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    print(f"{Colors.HEADER}Otonom Arka Plan Geliştirici Aktif. Sürekli çalışma moduna geçiliyor...{Colors.ENDC}")
    while True:
        run_simulation()
        print(f"Bir sonraki döngü için bekleniyor (3600 saniye / 1 saat)...")
        time.sleep(3600)  # Wait for 1 hour to prevent API rate limiting from NASA, etc.
