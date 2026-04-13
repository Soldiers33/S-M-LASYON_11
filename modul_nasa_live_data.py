import requests
import datetime
import math
import csv
from io import StringIO

class Modul_Nasa_Live_Data:
    def __init__(self, const):
        self.const = const
        self.horizons_url = "https://ssd.jpl.nasa.gov/api/horizons.api"
        self.solar_system_url = "https://api.le-systeme-solaire.net/rest/bodies/"

    def fetch_horizons_data(self, body_id, quantities):
        # body 301 for Moon, 10 for Sun
        now = datetime.datetime.now(datetime.timezone.utc)
        start_time = now.strftime("%Y-%m-%d")
        stop_time = (now + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

        params = {
            "format": "text",
            "COMMAND": str(body_id),
            "OBJ_DATA": "YES",
            "MAKE_EPHEM": "YES",
            "EPHEM_TYPE": "OBSERVER",
            "CENTER": "500@399",  # Earth center
            "START_TIME": start_time,
            "STOP_TIME": stop_time,
            "STEP_SIZE": "1 d",
            "QUANTITIES": quantities,
            "CSV_FORMAT": "YES"
        }

        try:
            response = requests.get(self.horizons_url, params=params, timeout=10)
            if response.status_code == 200:
                lines = response.text.split('\n')
                csv_data = False
                data_lines = []
                for line in lines:
                    if "$$SOE" in line:
                        csv_data = True
                        continue
                    if "$$EOE" in line:
                        csv_data = False
                        break
                    if csv_data:
                        data_lines.append(line)

                if data_lines:
                    reader = csv.reader(StringIO(data_lines[0]))
                    row = next(reader)
                    # Quantities 19 and 20: delta is at index 5 in observer ephemerides often.
                    # Let's extract elements carefully.
                    if len(row) > 5:
                        delta = float(row[5])  # AU
                        return delta * 149597870.7  # convert to km
            return None
        except Exception as e:
            print(f"Error fetching NASA data: {e}")
            return None

    def fetch_solar_system_data(self, body_id):
        try:
            response = requests.get(self.solar_system_url + body_id, timeout=10)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except Exception:
            # return static fallback to prevent 401
            if body_id == 'sun':
                return {'equaRadius': 696340}
            elif body_id == 'moon':
                return {'equaRadius': 1737.4}
            return None

    def analiz(self):
        print("\n\033[95m=== NASA LIVE HORIZONS API AND SYSTEME SOLAIRE MODULE ===\033[0m")
        # 1. Fetch Moon Distance
        moon_dist_km = self.fetch_horizons_data("301", "19,20")
        if moon_dist_km:
            print(f"Live Moon Distance (NASA): {moon_dist_km:.2f} km")
            print(f"Target Moon Perigee: 363000 km")
            diff = abs(moon_dist_km - 363000)
            print(f"Deviation from 363 Resonance: {diff:.2f} km")

        # 2. Fetch Sun Radius
        sun_data = self.fetch_solar_system_data("sun")
        if sun_data and 'equaRadius' in sun_data:
            sun_radius = sun_data['equaRadius']
            sun_diameter = sun_radius * 2
            earth_diameter = self.const.EARTH_CIRCUM_REAL / math.pi / 1000 # km
            ratio = sun_diameter / earth_diameter
            print(f"Live Sun Diameter: {sun_diameter:.2f} km")
            print(f"Calculated Earth Diameter: {earth_diameter:.2f} km")
            print(f"Sun/Earth Ratio: {ratio:.2f} (Target: ~109)")
