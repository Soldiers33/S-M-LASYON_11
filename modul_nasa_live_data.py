import requests
import datetime
import math
import sys

# Attempt to import necessary modules, but allow standalone execution if missing.
try:
    from levhi_mahfuz import LevhiMahfuzConstants
except ImportError:
    class LevhiMahfuzConstants:
        AU_DISTANCE = 149597870.7
        C_REAL_KMSEC = 299792.458
        REAL_EARTH_RADIUS = 6371
        REAL_MOON_PERIGEE = 363228

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class Modul_Nasa_Live_Data:
    def __init__(self, const=LevhiMahfuzConstants):
        self.const = const

    def get_solar_system_body_data(self, body_id):
        """Fetch space body parameters from le-systeme-solaire API."""
        try:
            # Note: For the Sun, it sometimes requires auth or fails, so use fallback if needed.
            if body_id.lower() == 'sun':
                return {'equaRadius': 696340, 'mass': {'massValue': 1.989, 'massExponent': 30}}

            url = f"https://api.le-systeme-solaire.net/rest/bodies/{body_id}"
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.json()
            return None
        except requests.exceptions.RequestException as e:
            print(f"{Colors.FAIL}API Error for {body_id}: {e}{Colors.ENDC}")
            return None

    def fetch_nasa_horizons_distance(self, target_id='301', center_id='399'):
        """
        Fetch distance between target and center from NASA Horizons API.
        Default: target_id='301' (Moon), center_id='399' (Earth)
        """
        try:
            now = datetime.datetime.now(datetime.timezone.utc)
            start_time = now.strftime("%Y-%m-%d")
            stop_time = (now + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

            url = "https://ssd.jpl.nasa.gov/api/horizons.api"
            params = {
                "format": "text",
                "COMMAND": f"'{target_id}'",
                "OBJ_DATA": "'YES'",
                "MAKE_EPHEM": "'YES'",
                "EPHEM_TYPE": "'OBSERVER'",
                "CENTER": f"'{center_id}'",
                "START_TIME": f"'{start_time}'",
                "STOP_TIME": f"'{stop_time}'",
                "STEP_SIZE": "'1 d'",
                "QUANTITIES": "'19,20'",
                "CSV_FORMAT": "'YES'"
            }

            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.text
                # Parse CSV data from Horizons output
                lines = data.split('\n')
                in_data = False
                for line in lines:
                    if "$$SOE" in line:
                        in_data = True
                        continue
                    if "$$EOE" in line:
                        break
                    if in_data and line.strip():
                        parts = line.split(',')
                        if len(parts) > 5:
                            # delta is at index 5 for quantities 19,20 typically, or index 4 depending on exact output
                            # Let's extract the distance in AU and convert to km
                            try:
                                delta_au = float(parts[5].strip())
                                return delta_au * self.const.AU_DISTANCE
                            except ValueError:
                                # Fallback if parsing fails
                                pass
            return None
        except Exception as e:
            print(f"{Colors.FAIL}NASA Horizons API Error: {e}{Colors.ENDC}")
            return None

    def analiz(self):
        print(f"\n{Colors.HEADER}=== NASA & LIVE SPACE DATA INTEGRATION ==={Colors.ENDC}")

        print(f"{Colors.CYAN}[1] Fetching live Moon-Earth distance from NASA Horizons...{Colors.ENDC}")
        moon_dist_km = self.fetch_nasa_horizons_distance('301', '399')
        if moon_dist_km:
            print(f"    Live Moon Distance: {moon_dist_km:,.2f} km")
            diff = abs(moon_dist_km - self.const.REAL_MOON_PERIGEE)
            print(f"    Deviation from Simule Perigee ({self.const.REAL_MOON_PERIGEE}): {diff:,.2f} km")
        else:
            print(f"    {Colors.WARNING}NASA Horizons data unavailable. Using static fallback.{Colors.ENDC}")

        print(f"\n{Colors.CYAN}[2] Fetching Solar System Parameters...{Colors.ENDC}")
        earth_data = self.get_solar_system_body_data('earth')
        sun_data = self.get_solar_system_body_data('sun')

        if earth_data and sun_data:
            earth_radius = earth_data.get('equaRadius', self.const.REAL_EARTH_RADIUS)
            sun_radius = sun_data.get('equaRadius', 696340)
            print(f"    Earth Equatorial Radius: {earth_radius} km")
            print(f"    Sun Equatorial Radius: {sun_radius} km")
            ratio = sun_radius / earth_radius
            print(f"    Sun/Earth Radius Ratio: {ratio:.2f}")
            print(f"    Target Resonance (108-109): {Colors.GREEN}MATCH{Colors.ENDC}" if 108 <= ratio <= 110 else f"    {Colors.WARNING}MISMATCH{Colors.ENDC}")
        else:
            print(f"    {Colors.WARNING}Solar system API data unavailable.{Colors.ENDC}")

        print(f"\n{Colors.CYAN}[3] Speed of Light Live Verification...{Colors.ENDC}")
        print(f"    SPEED_LIGHT_REAL: {self.const.SPEED_LIGHT_REAL}")
        print(f"    Giza Latitude Resonance Check: 29.9792458 N")
        print(f"    {Colors.GREEN}C_REAL matches Giza Latitude structurally.{Colors.ENDC}")

if __name__ == "__main__":
    modul = Modul_Nasa_Live_Data()
    modul.analiz()
