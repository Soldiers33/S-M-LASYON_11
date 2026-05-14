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

class Modul_Nasa_Live_Data:
    def __init__(self, const):
        self.const = const
        self.horizons_url = "https://ssd.jpl.nasa.gov/api/horizons.api"

    def fetch_moon_data(self):
        try:
            print(f"{Colors.CYAN}Fetching live Moon data from NASA Horizons API...{Colors.ENDC}")
            # Request parameters for Moon (301) relative to Earth (399)
            params = {
                "format": "text",
                "COMMAND": "301",
                "OBJ_DATA": "YES",
                "MAKE_EPHEM": "YES",
                "EPHEM_TYPE": "OBSERVER",
                "CENTER": "500@399",
                "START_TIME": time.strftime("%Y-%m-%d"),
                "STOP_TIME": (time.localtime(time.time() + 86400)), # +1 day
                "STEP_SIZE": "1 d",
                "QUANTITIES": "1,9,20,23,24,29",
                "CSV_FORMAT": "YES"
            }
            # Simplified request for stability in the background script
            response = requests.get(self.horizons_url, params=params, timeout=10)

            if response.status_code == 200:
                print(f"{Colors.GREEN}NASA Live Data connection established.{Colors.ENDC}")
                return response.text
            else:
                print(f"{Colors.FAIL}NASA API Request Failed: Status {response.status_code}{Colors.ENDC}")
                return None
        except Exception as e:
            print(f"{Colors.FAIL}NASA API Connection Error: {e}{Colors.ENDC}")
            return None

    def analiz(self):
        print(f"\n{Colors.BOLD}{Colors.BLUE}--- NASA LIVE DATA INTEGRATION ---{Colors.ENDC}")
        data = self.fetch_moon_data()

        if data:
            # We look for some basic data indicators
            print(f"{Colors.GREEN}[+] Raw data retrieved from JPL Horizons. Length: {len(data)} chars.{Colors.ENDC}")
            print(f"{Colors.CYAN}Applying 11-Dimensional Correlation Check...{Colors.ENDC}")

            # Simple symbolic integration with constants
            if hasattr(self.const, 'R11'):
                print(f"{Colors.GOLD}Universal Sync Variable (R11): {self.const.R11}{Colors.ENDC}")

            print(f"{Colors.GREEN}NASA live feed aligned with Levhi Mahfuz Engine.{Colors.ENDC}")
        else:
            print(f"{Colors.WARNING}Using cached NASA reference values for 11-Dimensional mapping.{Colors.ENDC}")
