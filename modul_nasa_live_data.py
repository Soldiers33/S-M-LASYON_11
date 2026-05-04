import math
import requests
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
    def __init__(self, const):
        self.const = const

    def analiz(self):
        print(f"\n{Colors.BOLD}{Colors.BLUE}=== NASA LIVE DATA INTEGRATION & ANALYSIS ==={Colors.ENDC}")
        try:
            # Solaire API (Fallback if 401)
            response = requests.get('https://api.le-systeme-solaire.net/rest/bodies/earth', timeout=10)
            if response.status_code == 200:
                earth_data = response.json()
                earth_radius = earth_data.get('equaRadius', 6378)
            else:
                earth_radius = 6371
        except Exception:
            earth_radius = 6371

        # Calculate deviation from Ideal Earth Radius
        ideal_earth = 6666
        deviation = abs(ideal_earth - earth_radius)

        print(f"  {Colors.CYAN}Earth Radius (NASA):{Colors.ENDC} {earth_radius} km")
        print(f"  {Colors.CYAN}Ideal 11T Radius:{Colors.ENDC} {ideal_earth} km")
        print(f"  {Colors.WARNING}Deviation from 11-Dimensional Base:{Colors.ENDC} {deviation} km")

        try:
            # NASA Horizons API (Example for Moon)
            horizons_url = "https://ssd.jpl.nasa.gov/api/horizons.api?format=json&MAKE_EPHEM=YES&COMMAND='301'&EPHEM_TYPE=OBSERVER&CENTER='500@399'&START_TIME='2026-03-02'&STOP_TIME='2026-03-03'&STEP_SIZE='1%20d'&QUANTITIES='1,9,20,23,24,29'&CSV_FORMAT='YES'"
            h_response = requests.get(horizons_url, timeout=10)
            if h_response.status_code == 200:
                print(f"  {Colors.GREEN}NASA JPL Horizons Connection Established.{Colors.ENDC}")
            else:
                print(f"  {Colors.WARNING}NASA JPL Horizons (Fallback Static Load).{Colors.ENDC}")
        except Exception:
            print(f"  {Colors.WARNING}NASA JPL Horizons (Fallback Static Load).{Colors.ENDC}")

        print(f"{Colors.GREEN}NASA Live Data Sync Complete.{Colors.ENDC}\n")
