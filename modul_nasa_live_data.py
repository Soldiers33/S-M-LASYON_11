import requests
import time
from levhi_mahfuz import LevhiMahfuzConstants
from simulasyon_11 import Colors

class Modul_NASA_LiveData:
    def __init__(self, const):
        self.const = const
        self.api_url = "https://api.le-systeme-solaire.net/rest/bodies/"
        print(f"\n{Colors.CYAN}[+] NASA / ASTRO Live Data Integration Module Initialized.{Colors.ENDC}")

    def fetch_data(self):
        print(f"{Colors.WARNING}[*] Fetching Live NASA / Open Data...{Colors.ENDC}")
        try:
            res_earth = requests.get(self.api_url + "terre", timeout=10)
            res_moon = requests.get(self.api_url + "lune", timeout=10)
            res_sun = requests.get(self.api_url + "soleil", timeout=10)

            earth_data = res_earth.json()
            moon_data = res_moon.json()

            try:
                sun_data = res_sun.json()
                sun_radius = sun_data.get('equaRadius', 696340)
            except:
                sun_radius = 696340 # Fallback

            print(f"{Colors.GREEN}[+] Live Data Retrieved Successfully!{Colors.ENDC}")

            earth_radius = earth_data.get('equaRadius', 6371)
            moon_radius = moon_data.get('equaRadius', 1737.4)

            print(f"    -> Earth Radius: {earth_radius} km (Simulated/Ideal: {LevhiMahfuzConstants.IDEAL_EARTH_RADIUS} km)")
            print(f"    -> Moon Radius: {moon_radius} km")
            print(f"    -> Sun Radius: {sun_radius} km")

            deviation = abs(LevhiMahfuzConstants.IDEAL_EARTH_RADIUS - earth_radius)
            print(f"    => Matrix Deviation (Earth): {deviation} km")

        except Exception as e:
            # Fallback data if API fails
            print(f"{Colors.FAIL}[-] API Error fetching data: {e}. Using static fallbacks.{Colors.ENDC}")
            print(f"    -> Earth Radius: 6371 km (Simulated/Ideal: {LevhiMahfuzConstants.IDEAL_EARTH_RADIUS} km)")
            print(f"    -> Moon Radius: 1737.4 km")
            print(f"    -> Sun Radius: 696340 km")
            deviation = abs(LevhiMahfuzConstants.IDEAL_EARTH_RADIUS - 6371)
            print(f"    => Matrix Deviation (Earth): {deviation} km")

    def analiz(self):
        self.fetch_data()
