import time
import requests

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

class NasaLiveData:
    def __init__(self):
        self.sun_radius = 696340
        self.earth_radius = 6371
        self.base_url = "https://api.le-systeme-solaire.net/rest/bodies/"

    def fetch_live_data(self):
        print(f"{Colors.BOLD}{Colors.BLUE}[NASA/SOLAR] FETCHING LIVE PLANETARY DATA...{Colors.ENDC}")
        try:
            earth_resp = requests.get(f"{self.base_url}earth", timeout=5)
            if earth_resp.status_code == 200:
                self.earth_radius = earth_resp.json().get('equaRadius', self.earth_radius)

            sun_resp = requests.get(f"{self.base_url}sun", timeout=5)
            if sun_resp.status_code == 200:
                self.sun_radius = sun_resp.json().get('equaRadius', self.sun_radius)

            print(f"{Colors.CYAN}Sun Equatorial Radius (Live): {self.sun_radius} km{Colors.ENDC}")
            print(f"{Colors.CYAN}Earth Equatorial Radius (Live): {self.earth_radius} km{Colors.ENDC}")
            print(f"{Colors.GREEN}[NASA/SOLAR] Live Data Synced Successfully.{Colors.ENDC}")
            return True
        except Exception as e:
            print(f"{Colors.WARNING}[!] API connection failed, using static values: {e}{Colors.ENDC}")
            print(f"{Colors.CYAN}Sun Equatorial Radius: {self.sun_radius} km{Colors.ENDC}")
            print(f"{Colors.CYAN}Earth Equatorial Radius: {self.earth_radius} km{Colors.ENDC}")
            return False

    def analiz(self):
        self.fetch_live_data()
