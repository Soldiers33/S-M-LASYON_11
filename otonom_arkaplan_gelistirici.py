import time
import os
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
    MAGENTA = '\033[35m'
    GOLD = '\033[33m'

def baslat():
    print(f"\n{Colors.BOLD}{Colors.GOLD}[=== OTONOM ARKA PLAN GELİSTİRİCİ (BACKGROUND DEVELOPER AI) ===]{Colors.ENDC}")
    print(f"{Colors.CYAN}Durum: AKTİF (Sürekli Gelişim Modu){Colors.ENDC}")
    print(f"{Colors.CYAN}Hedef: NASA, ArXiv ve Veri Doğrulama Modüllerini entegre ederek Simülasyonu periyodik olarak çalıştırmak.{Colors.ENDC}\n")

    while True:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        print(f"{Colors.MAGENTA}[{timestamp}] Otonom Döngü Başlıyor...{Colors.ENDC}")

        try:
            print(f"{Colors.BLUE}[*] Simulasyon_11.py tetikleniyor...{Colors.ENDC}")
            # Run the main orchestrator script and capture some output or let it run
            # We use os.system here to execute the python file directly
            exit_code = os.system(f"{sys.executable} simulasyon_11.py > arkaplan_output.log 2>&1")

            if exit_code == 0:
                print(f"{Colors.GREEN}[+] Simülasyon başarıyla tamamlandı. Loglar 'arkaplan_output.log' dosyasına yazıldı.{Colors.ENDC}")
            else:
                print(f"{Colors.WARNING}[!] Simülasyon çalıştırılırken bir hata oluştu (Çıkış Kodu: {exit_code}). Logları kontrol edin.{Colors.ENDC}")

        except Exception as e:
            print(f"{Colors.FAIL}[X] Kritik Döngü Hatası: {str(e)}{Colors.ENDC}")

        print(f"{Colors.CYAN}[*] Arka plan geliştirici 1 saat (3600 sn) uykuya geçiyor (API Limitleri İçin)...{Colors.ENDC}\n")
        # Sleep for an hour to prevent hitting rate limits
        time.sleep(3600)

if __name__ == '__main__':
    baslat()
