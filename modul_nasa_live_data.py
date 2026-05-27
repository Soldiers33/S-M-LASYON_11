import requests
import datetime
import math
import csv
from io import StringIO

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

class Modul_NASA_LiveData:
    """
    Fetches real-time data from NASA JPL Horizons API.
    Looks for correlations with the 11-dimensional framework.
    """
    def __init__(self):
        self.api_url = "https://ssd.jpl.nasa.gov/api/horizons.api"

    def fetch_moon_data(self):
        print(f"{Colors.BLUE}[NASA API] Fetching live Moon ephemeris data...{Colors.ENDC}")
        # Moon ID = 301, Earth center = '500@399'
        now = datetime.datetime.utcnow()
        start_time = now.strftime('%Y-%m-%d')
        end_time = (now + datetime.timedelta(days=1)).strftime('%Y-%m-%d')

        params = {
            'format': 'text',
            'COMMAND': "'301'",
            'OBJ_DATA': "'YES'",
            'MAKE_EPHEM': "'YES'",
            'EPHEM_TYPE': "'OBSERVER'",
            'CENTER': "'500@399'",
            'START_TIME': f"'{start_time}'",
            'STOP_TIME': f"'{end_time}'",
            'STEP_SIZE': "'1 d'",
            'QUANTITIES': "'1,19,20'", # Astrometric RA/DEC, Earth-Obs range
            'CSV_FORMAT': "'YES'"
        }

        try:
            response = requests.get(self.api_url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.text
                return self.parse_horizons_csv(data)
            else:
                print(f"{Colors.WARNING}[NASA API] Failed to fetch data: HTTP {response.status_code}{Colors.ENDC}")
                return None
        except Exception as e:
            print(f"{Colors.FAIL}[NASA API] Connection error: {e}{Colors.ENDC}")
            return None

    def parse_horizons_csv(self, text_data):
        """Extract variables from Horizons CSV output."""
        # Find the $$SOE (Start of Ephemeris) and $$EOE (End of Ephemeris)
        try:
            start_idx = text_data.find("$$SOE") + 5
            end_idx = text_data.find("$$EOE")
            if start_idx == 4 or end_idx == -1:
                return None

            csv_data = text_data[start_idx:end_idx].strip()
            # Read first line of data
            f = StringIO(csv_data)
            reader = csv.reader(f)
            row = next(reader)

            # Extract distance (delta) - usually the last columns depending on QUANTITIES
            # We requested 1,19,20. Range (delta) in AU is typically around column 5 or 6
            # after Date, RA, DEC, etc.
            # Let's extract values dynamically or return the raw row for processing.
            distance_au = 0.002569 # fallback approx for moon distance in AU

            for col in row:
                try:
                    val = float(col.strip())
                    if 0.001 < val < 0.003: # likely Moon distance in AU
                        distance_au = val
                except ValueError:
                    continue

            distance_km = distance_au * 149597870.7 # Convert AU to km
            return {"moon_distance_km": distance_km, "moon_distance_au": distance_au}

        except Exception as e:
            print(f"{Colors.FAIL}[NASA API] Parse error: {e}{Colors.ENDC}")
            return None

    def analiz(self):
        print(f"\n{Colors.HEADER}=== MODUL_NASA_LIVEDATA: 11-DIMENSIONAL CORRELATION ==={Colors.ENDC}")
        data = self.fetch_moon_data()

        results = {}
        if data:
            dist_km = data.get("moon_distance_km", 384400)
            print(f"Live Moon Distance: {dist_km:,.2f} km")

            # Check for 11 resonance
            ideal_perigee = 363000 # 33 * 11000
            diff = abs(dist_km - ideal_perigee)
            resonance = diff % 11

            print(f"Variance from Ideal 11T Perigee (363,000 km): {diff:,.2f} km")
            print(f"11-Resonance Index: {resonance:.2f} (closer to 0 is stronger)")
            results["live_moon_distance_km"] = dist_km
            results["variance_from_11T"] = diff
            results["resonance_11"] = resonance

        return results
