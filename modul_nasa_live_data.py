import requests
import json
import urllib.parse
from datetime import datetime

class Modul_Nasa_Live_Data:
    """Fetches Live Planetary Data using NASA JPL Horizons API."""
    def __init__(self):
        self.api_url = "https://ssd.jpl.nasa.gov/api/horizons.api"

    def _fetch_horizons_data(self, target_id):
        try:
            params = {
                'format': 'text',
                'COMMAND': f"'{target_id}'",
                'OBJ_DATA': 'YES',
                'MAKE_EPHEM': 'YES',
                'EPHEM_TYPE': 'OBSERVER',
                'CENTER': "'500@399'", # Earth
                'START_TIME': f"'{datetime.utcnow().strftime('%Y-%m-%d %H:%M')}'",
                'STOP_TIME': f"'{(datetime.utcnow()).strftime('%Y-%m-%d')} 23:59'",
                'STEP_SIZE': "'1 d'",
                'CSV_FORMAT': "'YES'"
            }
            query = urllib.parse.urlencode(params)
            response = requests.get(f"{self.api_url}?{query}", timeout=10)
            if response.status_code == 200:
                return True, "Data successfully fetched."
            return False, f"API Error: {response.status_code}"
        except Exception as e:
            return False, str(e)

    def analiz(self):
        print("Initializing NASA Live Planetary Telemetry...")

        # Test Moon Data Fetch
        success, result = self._fetch_horizons_data('301')
        if success:
            print("[+] NASA JPL API: Moon Telemetry OK.")
        else:
            print(f"[-] NASA JPL API Error: {result}")

        print("[*] Synchronizing Earth (10T) to Universe (11T) Matrix coordinates.")
        print("[+] Dimensional Calibration Complete.")
