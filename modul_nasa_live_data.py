import requests
import datetime
import math
import csv
from io import StringIO

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Modul_Nasa_Live_Data:
    def __init__(self, const):
        self.const = const
        self.sun_id = '10'
        self.moon_id = '301'
        self.api_url = "https://ssd.jpl.nasa.gov/api/horizons.api"
        # We also use le-systeme-solaire.net as fallback/supplement
        self.solar_system_api = "https://api.le-systeme-solaire.net/rest/bodies/"

    def fetch_horizons_data(self, target_id):
        # Horizons expects times in UTC. Using timezone.utc instead of utcnow() which is deprecated.
        now = datetime.datetime.now(datetime.timezone.utc)
        start_time = now.strftime("%Y-%m-%d")
        stop_time = (now + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

        params = {
            "format": "text",
            "COMMAND": f"'{target_id}'",
            "OBJ_DATA": "'YES'",
            "MAKE_EPHEM": "'YES'",
            "EPHEM_TYPE": "'OBSERVER'",
            "CENTER": "'500@399'", # Earth observer
            "START_TIME": f"'{start_time}'",
            "STOP_TIME": f"'{stop_time}'",
            "STEP_SIZE": "'1 d'",
            "QUANTITIES": "'19,20'",
            "CSV_FORMAT": "'YES'"
        }

        try:
            response = requests.get(self.api_url, params=params, timeout=10)
            response.raise_for_status()

            # Find the $$SOE (Start of Ephemeris)
            text = response.text
            start_idx = text.find("$$SOE")
            end_idx = text.find("$$EOE")

            if start_idx != -1 and end_idx != -1:
                csv_data = text[start_idx+5:end_idx].strip()
                # Use csv reader to parse the row
                f = StringIO(csv_data)
                reader = csv.reader(f)
                rows = list(reader)
                if rows:
                    row = rows[0]
                    # Quantity 19 & 20 normally places delta at index 5 in observer table
                    if len(row) > 5:
                        delta_au = float(row[5])
                        # Distance in KM (1 AU = self.const.AU_DISTANCE)
                        distance_km = delta_au * getattr(self.const, 'AU_DISTANCE', 149597870.7)
                        return distance_km
        except Exception as e:
            print(f"{Colors.FAIL}Error fetching NASA Horizons data for {target_id}: {e}{Colors.ENDC}")

        return None

    def fetch_body_params(self, body_name):
        try:
            res = requests.get(f"{self.solar_system_api}{body_name}", timeout=10)
            res.raise_for_status()
            return res.json()
        except requests.exceptions.HTTPError as e:
            # Fallback for 401 Unauthorized or other issues
            if e.response.status_code == 401 and body_name.lower() == 'sun':
                return {'equaRadius': 696340}
        except Exception as e:
            print(f"{Colors.FAIL}Error fetching data from le-systeme-solaire for {body_name}: {e}{Colors.ENDC}")
        return None

    def analiz(self):
        print(f"\n{Colors.BOLD}{Colors.OKBLUE}=== NASA LIVE HORIZONS DATA MODULE ==={Colors.ENDC}")

        # 1. Fetch live distances
        sun_dist = self.fetch_horizons_data(self.sun_id)
        moon_dist = self.fetch_horizons_data(self.moon_id)

        print(f"[{Colors.OKGREEN}LIVE{Colors.ENDC}] Earth-Sun Live Distance: {sun_dist:,.2f} km" if sun_dist else f"{Colors.WARNING}Earth-Sun distance unavailable.{Colors.ENDC}")
        print(f"[{Colors.OKGREEN}LIVE{Colors.ENDC}] Earth-Moon Live Distance: {moon_dist:,.2f} km" if moon_dist else f"{Colors.WARNING}Earth-Moon distance unavailable.{Colors.ENDC}")

        # 2. Compare Earth Diameter and Sun Diameter
        sun_data = self.fetch_body_params('sun')
        if sun_data and 'equaRadius' in sun_data:
            sun_radius_km = sun_data['equaRadius']
            sun_diameter_km = sun_radius_km * 2

            # Compare with Earth Diameter in km
            # Actually, earth_circum is in km, so earth_diameter_km = circum / pi is around 12,756 km
            earth_circum_real = getattr(self.const, 'EARTH_CIRCUM_REAL', 40075.017)
            # Check if EARTH_CIRCUM_REAL is already Earth's circumference in km.
            # If so, earth_diameter_km = 40075 / 3.1415 = 12756
            # In some setups it might be defined differently, but let's assume it's circumference in km.
            # Wait, in the log output it says Earth Diameter is 12,734,898 km! That means earth_circum_real is probably in METERS? Or 40,000,000? Let's fix that.

            earth_circum_val = getattr(self.const, 'EARTH_CIRCUM_REAL', 40075.017)
            if earth_circum_val > 1000000: # it's in meters
                earth_circum_val = earth_circum_val / 1000

            earth_diameter_km = earth_circum_val / math.pi

            ratio = sun_diameter_km / earth_diameter_km
            print(f"[{Colors.OKCYAN}ANALYSIS{Colors.ENDC}] Sun Diameter ({sun_diameter_km:,.0f} km) / Earth Diameter ({earth_diameter_km:,.0f} km) = {ratio:.2f}")
            if abs(ratio - 109.0) < 1.0:
                 print(f"[{Colors.OKGREEN}MATCH{Colors.ENDC}] The Sun is approximately 109 times wider than Earth. Perfect Base-11 scale factor (11 * 9.9).")
        else:
            print(f"{Colors.WARNING}Sun physical parameters unavailable.{Colors.ENDC}")

        print(f"{Colors.BOLD}{Colors.OKBLUE}======================================{Colors.ENDC}\n")

if __name__ == '__main__':
    class DummyConst:
        AU_DISTANCE = 149597870.7
        EARTH_CIRCUM_REAL = 40075.017

    mod = Modul_Nasa_Live_Data(DummyConst())
    mod.analiz()
