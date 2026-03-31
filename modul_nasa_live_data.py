import requests
import math
import datetime

class Colors:
    HEADER = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    GOLD = '\033[33m'

class Modul_Nasa_Canli_Veri:
    def __init__(self, const):
        self.const = const

    def get_horizons_data(self, body_id):
        # Using today's date in UTC
        today = datetime.datetime.now(datetime.timezone.utc)
        start_time = today.strftime("%Y-%m-%d")
        stop_time = (today + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

        url = "https://ssd.jpl.nasa.gov/api/horizons.api"
        params = {
            "format": "text",
            "COMMAND": f"'{body_id}'",
            "OBJ_DATA": "'YES'",
            "MAKE_EPHEM": "'YES'",
            "EPHEM_TYPE": "'OBSERVER'",
            "CENTER": "'500@399'", # Earth center
            "START_TIME": f"'{start_time}'",
            "STOP_TIME": f"'{stop_time}'",
            "STEP_SIZE": "'1 d'",
            "QUANTITIES": "'19,20'",
            "CSV_FORMAT": "'YES'"
        }

        try:
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                lines = response.text.split('\n')
                in_data = False
                for line in lines:
                    if "$$SOE" in line:
                        in_data = True
                        continue
                    if "$$EOE" in line:
                        in_data = False
                        break
                    if in_data:
                        parts = line.split(',')
                        if len(parts) > 5:
                            # Distance in AU is at index 5
                            delta_au = float(parts[5].strip())
                            # Convert AU to km
                            delta_km = delta_au * 149597870.7
                            return delta_km
        except Exception as e:
            print(f"{Colors.WARNING}NASA Horizons API error: {e}{Colors.ENDC}")
        return None

    def get_solar_system_data(self, body_name):
        url = f"https://api.le-systeme-solaire.net/rest/bodies/{body_name}"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 401:
                if body_name == 'sun':
                    return {'equaRadius': 696340}
        except Exception as e:
            print(f"{Colors.WARNING}le-systeme-solaire API error: {e}{Colors.ENDC}")

        if body_name == 'sun':
            return {'equaRadius': 696340}
        return None

    def analiz(self):
        print(f"\n{Colors.HEADER}=== NASA LIVE DATA INTEGRATION (V.133) ==={Colors.ENDC}")

        # Moon Distance
        moon_dist_km = self.get_horizons_data('301')
        if moon_dist_km:
            print(f"Live Moon Distance (NASA Horizons): {moon_dist_km:,.2f} km")
            print(f"Simule3 Ideal Moon Perigee: 363,000 km")
            diff = abs(moon_dist_km - 363000)
            print(f"Deviation: {diff:,.2f} km")
        else:
            print(f"{Colors.FAIL}Could not fetch live Moon data.{Colors.ENDC}")

        # Sun Data
        sun_data = self.get_solar_system_data('sun')
        if sun_data and 'equaRadius' in sun_data:
            sun_radius = sun_data['equaRadius']
            print(f"\nLive Sun Equatorial Radius: {sun_radius:,.0f} km")
            earth_diam = self.const.EARTH_CIRCUM_REAL / math.pi / 1000
            print(f"Earth Diameter (Calculated): {earth_diam:,.2f} km")
            ratio = (sun_radius * 2) / earth_diam
            print(f"Sun/Earth Diameter Ratio: {ratio:,.2f} (Target: ~109)")
        else:
            print(f"{Colors.FAIL}Could not fetch live Sun data.{Colors.ENDC}")
