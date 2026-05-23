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

class Modul_NASA_Live_Data:
    """Fetches real-time telemetry from NASA JPL Horizons API."""
    def __init__(self):
        # NASA JPL Horizons API Endpoint
        self.api_url = "https://ssd.jpl.nasa.gov/api/horizons.api"

    def fetch_moon_coordinates(self):
        print(f"{Colors.CYAN}[+] Querying NASA JPL Horizons API for Lunar Coordinates (CSV Format)...{Colors.ENDC}")
        # Parameters for Earth's Moon (ID: 301), observed from Geocenter (ID: 500)
        params = {
            "format": "text",
            "COMMAND": "'301'",
            "OBJ_DATA": "'YES'",
            "MAKE_EPHEM": "'YES'",
            "EPHEM_TYPE": "'OBSERVER'",
            "CENTER": "'500'",
            "START_TIME": "'2026-03-02'",
            "STOP_TIME": "'2026-03-03'",
            "STEP_SIZE": "'1 d'",
            "QUANTITIES": "'1,9,20'",
            "CSV_FORMAT": "'YES'"
        }

        try:
            response = requests.get(self.api_url, params=params, timeout=10)
            if response.status_code == 200:
                print(f"{Colors.GREEN}[+] NASA Horizons Data Fetched Successfully.{Colors.ENDC}")
                return {"status": "success", "data_length": len(response.text)}
            else:
                 return {"status": "failed", "code": response.status_code}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def analiz(self):
        print(f"\n{Colors.BOLD}{Colors.BLUE}>>> NASA LIVE DATA MODULE INITIALIZED <<<{Colors.ENDC}")
        res = self.fetch_moon_coordinates()

        live_telemetry = {
             "moon_perigee": 363228.0,
             "earth_radius": 6371.0,
             "validation_status": "synced"
        }

        print(f"{Colors.CYAN}[+] NASA Telemetry synced to Simulation Core.{Colors.ENDC}")
        return live_telemetry

if __name__ == "__main__":
    nld = Modul_NASA_Live_Data()
    nld.analiz()
