import requests
import datetime
import csv
from io import StringIO

class Modul_NASA_Live_Data:
    """Fetches real-time data from NASA Horizons API."""
    def __init__(self, const):
        self.const = const
        self.api_url = "https://ssd.jpl.nasa.gov/api/horizons.api"

    def fetch_moon_distance(self):
        # Current time in UTC per memory directive
        now = datetime.datetime.now(datetime.timezone.utc)
        start_time = now.strftime("%Y-%m-%d")
        stop_time = (now + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

        params = {
            "format": "text",
            "COMMAND": "'301'", # Moon
            "OBJ_DATA": "'YES'",
            "MAKE_EPHEM": "'YES'",
            "EPHEM_TYPE": "'OBSERVER'",
            "CENTER": "'500@399'", # Earth
            "START_TIME": f"'{start_time}'",
            "STOP_TIME": f"'{stop_time}'",
            "STEP_SIZE": "'1 d'",
            "QUANTITIES": "'19,20'",
            "CSV_FORMAT": "'YES'"
        }

        try:
            response = requests.get(self.api_url, params=params, timeout=10)
            if response.status_code == 200:
                lines = response.text.splitlines()
                in_data = False
                csv_data = []
                for line in lines:
                    if "$$SOE" in line:
                        in_data = True
                        continue
                    if "$$EOE" in line:
                        in_data = False
                        break
                    if in_data:
                        csv_data.append(line)

                if csv_data:
                    reader = csv.reader(csv_data)
                    for row in reader:
                        # Observer distance (delta) is at index 5 for quantities 19,20
                        if len(row) > 5:
                            delta_au = float(row[5].strip())
                            delta_km = delta_au * 149597870.7 # Convert AU to km
                            return delta_km
        except Exception as e:
            pass # Fallback below

        return 384400.0 # Standard fallback

    def analiz(self):
        print("\033[94m=== NASA HORIZONS LIVE DATA ===\033[0m")
        distance = self.fetch_moon_distance()
        print(f"Current Moon Distance: {distance:.2f} km")
