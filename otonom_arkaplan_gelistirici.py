import time
import sys
from simulasyon_11 import Simule3_Lab_V133, Colors
from modul_nasa_live_data import Modul_NASA_LiveData
from deep_research_module import Modul_Deep_Research

class Otonom_Arka_Plan:
    def __init__(self, main_sim):
        self.sim = main_sim
        self.nasa_modul = Modul_NASA_LiveData(main_sim.const)
        self.research_modul = Modul_Deep_Research(main_sim.const)

    def baslat(self):
        print(f"\n{Colors.BOLD}{Colors.PURPLE}=== OTONOM ARKA PLAN GELİSTİRİCİ BAŞLATILDI ==={Colors.ENDC}")
        print("Sistem siz yokken arka planda çalışıp araştırmalara devam edecek.")

        loop_count = 0
        while True:
            loop_count += 1
            print(f"\n{Colors.BLUE}--- DONGU #{loop_count} ---{Colors.ENDC}")

            # 1. NASA Live Data Analysis
            self.nasa_modul.analiz()

            # 2. Deep Research / Discovery Simulation
            self.research_modul.analiz()

            # 3. Main Simulation Execution
            self.sim.run_all()

            print(f"{Colors.GREEN}[+] Dongu #{loop_count} Tamamlandi. Bekleniyor...{Colors.ENDC}")
            time.sleep(3) # Wait 3 seconds before next iteration

if __name__ == '__main__':
    sim = Simule3_Lab_V133()
    otonom = Otonom_Arka_Plan(sim)
    try:
        otonom.baslat()
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}Otonom Arka Plan Geliştirici durduruldu.{Colors.ENDC}")
        sys.exit(0)
