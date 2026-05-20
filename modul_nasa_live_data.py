import requests
import json
import urllib.parse
from datetime import datetime, timedelta

class Modul_NasaLiveData:
    def __init__(self, const):
        self.const = const

    def analiz(self):
        print("\033[96m[NASA LIVE DATA] Fetching live coordinates from NASA JPL Horizons API...\033[0m")
        # Halley's Comet (Target body 90000033)
        # We query for current time
        now = datetime.utcnow()
        start_time = now.strftime('%Y-%m-%d')
        stop_time = (now + timedelta(days=1)).strftime('%Y-%m-%d')

        # Build JPL Horizons query
        url = "https://ssd.jpl.nasa.gov/api/horizons.api"
        params = {
            "format": "text",
            "COMMAND": "'90000033'",  # Halley's Comet
            "OBJ_DATA": "'YES'",
            "MAKE_EPHEM": "'YES'",
            "EPHEM_TYPE": "'OBSERVER'",
            "CENTER": "'500@399'", # Earth
            "START_TIME": f"'{start_time}'",
            "STOP_TIME": f"'{stop_time}'",
            "STEP_SIZE": "'1 d'",
            "CSV_FORMAT": "'YES'"
        }

        try:
            query_string = urllib.parse.urlencode(params)
            full_url = f"{url}?{query_string}"
            response = requests.get(full_url, timeout=10)
            if response.status_code == 200:
                print("\033[92m[OK] Successfully retrieved live data from NASA JPL Horizons.\033[0m")
                # Very simple parse just to show it works
                data = response.text
                if "CSV_FORMAT" in data or "$$SOE" in data:
                     print("\033[92m[OK] Data format is correct (CSV).\033[0m")
            else:
                print(f"\033[93m[WARNING] NASA JPL API returned status code {response.status_code}\033[0m")
        except Exception as e:
            print(f"\033[93m[WARNING] Could not fetch NASA data: {e}\033[0m")
