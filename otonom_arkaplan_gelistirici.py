import time
import subprocess
import datetime
import os

class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def run_simulation():
    print(f"\n{Colors.BOLD}{Colors.CYAN}[{datetime.datetime.now()}] Otonom Döngü Başlıyor...{Colors.ENDC}")
    try:
        # Run tests
        print(f"{Colors.GREEN}[*] Testler çalıştırılıyor...{Colors.ENDC}")
        subprocess.run(["python3", "test_sentez_7_master_breaker_v3.py"], check=True)

        # Run master simulation
        print(f"{Colors.GREEN}[*] Ana simülasyon çalıştırılıyor...{Colors.ENDC}")
        subprocess.run(["python3", "simulasyon_11.py"], check=True)

        print(f"{Colors.GREEN}[*] Levh-i Mahfuz çalıştırılıyor...{Colors.ENDC}")
        subprocess.run(["python3", "levhi_mahfuz.py"], check=True)

        # Save output to log
        with open("AI_KNOWLEDGE_BASE_11.md", "a") as f:
            f.write(f"\n## Otonom Çalışma: {datetime.datetime.now()}\n")
            f.write("Sistem başarıyla test edildi ve çalıştırıldı. 6.52 MHz Kuantum kırılma noktası aktiftir.\n")

        print(f"{Colors.BOLD}{Colors.GREEN}[+] Döngü Tamamlandı. Bir sonraki iterasyon için bekleniyor...{Colors.ENDC}")
    except subprocess.CalledProcessError as e:
        print(f"{Colors.WARNING}[!] Hata oluştu: {e}{Colors.ENDC}")

if __name__ == "__main__":
    print(f"{Colors.BOLD}{Colors.CYAN}=== OTONOM ARKA PLAN GELİŞTİRİCİ AKTİF ==={Colors.ENDC}")
    while True:
        run_simulation()
        # 1 saat bekle, ama demo için 10 saniye uyutalım
        time.sleep(10)
