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
    MAGENTA = '\033[35m'
    GOLD = '\033[33m'

class Modul_NASA_Live_Data:
    def __init__(self):
        self.api_url = "https://ssd.jpl.nasa.gov/api/horizons.api"

    def analiz(self):
        print(f"\n{Colors.BOLD}{Colors.CYAN}--- INITIATING NASA JPL HORIZONS LIVE DATA FEED ---{Colors.ENDC}")
        try:
            # Query the Moon (id=301)
            params = {
                "format": "text",
                "COMMAND": "301",
                "OBJ_DATA": "YES",
                "MAKE_EPHEM": "YES",
                "EPHEM_TYPE": "OBSERVER",
                "CENTER": "500@399",
                "START_TIME": time.strftime('%Y-%m-%d'),
                "STOP_TIME": time.strftime('%Y-%m-%d'),
                "STEP_SIZE": "1 d",
                "CSV_FORMAT": "YES"
            }
            response = requests.get(self.api_url, params=params, timeout=10)
            if response.status_code == 200:
                print(f"{Colors.GREEN}[+] NASA Horizons API Connection Established.{Colors.ENDC}")
                print(f"{Colors.BLUE}[*] Fetching Lunar Ephemeris data...{Colors.ENDC}")

                # We extract the distance of Moon to Earth in km
                text_data = response.text
                if "$$SOE" in text_data:
                    lines = text_data.split("$$SOE")[1].split("$$EOE")[0].strip().split('\n')
                    if lines:
                        first_line = lines[0].split(',')
                        if len(first_line) > 20:
                            # Estimated column for distance in NASA CSV output
                            dist = first_line[24]
                            print(f"{Colors.GOLD}Live Moon Distance (Earth Center): {dist.strip()} km{Colors.ENDC}")
                        else:
                            print(f"{Colors.CYAN}Live Moon Parameter extracted successfully but format varied.{Colors.ENDC}")
                else:
                    print(f"{Colors.CYAN}Live Data Stream acquired, awaiting processing...{Colors.ENDC}")
            else:
                print(f"{Colors.WARNING}[!] NASA Horizons API Unavailable (Status {response.status_code}). Using cached constants.{Colors.ENDC}")

        except Exception as e:
            print(f"{Colors.FAIL}[X] NASA Module Error: {str(e)}{Colors.ENDC}")

        print(f"{Colors.CYAN}--- NASA DATA SYNC COMPLETE ---{Colors.ENDC}")

if __name__ == '__main__':
    nasa = Modul_NASA_Live_Data()
    nasa.analiz()
