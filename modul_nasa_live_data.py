import requests
import json
import time

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

class Modul_Nasa_Live_Data:
    def __init__(self):
        self.api_url = "https://api.le-systeme-solaire.net/rest/bodies/"
        self.solar_system_data = {}
        self.fallback_data = {
            "earth": {"equaRadius": 6371.0, "meanRadius": 6371.0},
            "moon": {"equaRadius": 1737.4, "meanRadius": 1737.4},
            "sun": {"equaRadius": 696340.0, "meanRadius": 696340.0}
        }

    def fetch_data(self):
        print(f"{Colors.CYAN}[NASA LIVE DATA] Otonom veri çekimi başlatılıyor...{Colors.ENDC}")
        try:
            response_earth = requests.get(self.api_url + "terre", timeout=5)
            response_moon = requests.get(self.api_url + "lune", timeout=5)

            if response_earth.status_code == 200 and response_moon.status_code == 200:
                self.solar_system_data["earth"] = response_earth.json()
                self.solar_system_data["moon"] = response_moon.json()
                print(f"{Colors.GREEN}[NASA LIVE DATA] Veri başarıyla çekildi.{Colors.ENDC}")
            else:
                print(f"{Colors.WARNING}[NASA LIVE DATA] API Hatası, fallback verileri kullanılıyor.{Colors.ENDC}")
                self.solar_system_data = self.fallback_data

        except Exception as e:
            print(f"{Colors.WARNING}[NASA LIVE DATA] Hata: {str(e)}. Fallback verileri kullanılıyor.{Colors.ENDC}")
            self.solar_system_data = self.fallback_data

    def analiz(self):
        self.fetch_data()

        earth_r = self.solar_system_data.get("earth", {}).get("equaRadius", 6371.0)
        moon_r = self.solar_system_data.get("moon", {}).get("equaRadius", 1737.4)
        sun_r = self.fallback_data["sun"]["equaRadius"]

        print(f"\n{Colors.BOLD}{Colors.PURPLE}=== NASA LIVE DATA SENTEZ ANALİZİ ==={Colors.ENDC}")
        print(f"Dünya Ekvator Yarıçapı: {earth_r} km")
        print(f"Ay Ekvator Yarıçapı: {moon_r} km")
        print(f"Dünya/Ay Oranı: {earth_r / moon_r:.4f}")

        # Simule3 3.63 Hatay/Ay kodu check
        target_ratio = 3.63
        diff = abs((earth_r / moon_r) - target_ratio)

        print(f"Simüle 11 Hedef Oranı: {target_ratio}")
        print(f"Sapma (Glitch Margin): {diff:.4f}")
        print(f"{Colors.GREEN}[+] NASA Data Integration Complete.{Colors.ENDC}\n")

if __name__ == "__main__":
    nasa = Modul_Nasa_Live_Data()
    nasa.analiz()
