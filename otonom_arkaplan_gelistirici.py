import time
import datetime
import sys

# Import the core simulation execution class
try:
    from simulasyon_11 import Simule3_Lab_V133, Colors
except ImportError:
    print("CRITICAL: Failed to import simulasyon_11. Make sure the file exists.")
    sys.exit(1)

def run_background_simulation_loop():
    print(f"\n{Colors.HEADER}=== OTONOM ARKA PLAN GELİŞTİRİCİ BAŞLATILDI ==={Colors.ENDC}")
    print(f"Başlangıç Zamanı: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Sistem sürekli olarak (arka planda) evrensel verileri tarayacak ve simülasyonu güncelleyecektir...\n")

    iteration = 1
    # Run the loop forever to fulfill continuous background processing requirements
    while True:
        print(f"\n{Colors.BOLD}{Colors.CYAN}--- DÖNGÜ: {iteration} | TARİH: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---{Colors.ENDC}")

        try:
            # Initialize and run the master simulation kernel
            lab = Simule3_Lab_V133()
            lab.run_all()

            print(f"\n{Colors.GREEN}[Döngü {iteration} Başarıyla Tamamlandı]{Colors.ENDC}")
        except Exception as e:
            print(f"\n{Colors.FAIL}[HATA] Simülasyon döngüsünde istisna oluştu: {e}{Colors.ENDC}")

        iteration += 1

        # Pause for 11 minutes (660 seconds) between cycles as requested by theory
        print(f"{Colors.WARNING}Sistem 11 dakika boyunca otonom veri toplayıp dinleniyor...{Colors.ENDC}")
        time.sleep(660)

if __name__ == "__main__":
    run_background_simulation_loop()
