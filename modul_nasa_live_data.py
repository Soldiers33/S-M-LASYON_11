import requests
import datetime
import math

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

class Modul_Nasa_Live_Data:
    """
    Fetches live data from NASA Horizons API and Le Systeme Solaire API
    Integrates live parameters with base-11 quantum simulation constants
    """
    def __init__(self, const):
        self.const = const
        self.horizons_url = "https://ssd.jpl.nasa.gov/api/horizons.api"
        self.solar_system_url = "https://api.le-systeme-solaire.net/rest/bodies/"

    def fetch_horizons_data(self, command, name):
        """Fetches distance (delta) from NASA JPL Horizons API"""
        print(f"Fetching real-time data for {name} from NASA Horizons...")

        now = datetime.datetime.now(datetime.timezone.utc)
        start_time = now.strftime("%Y-%m-%d")
        stop_time = (now + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

        params = {
            "format": "json",
            "COMMAND": f"'{command}'",
            "OBJ_DATA": "'YES'",
            "MAKE_EPHEM": "'YES'",
            "EPHEM_TYPE": "'OBSERVER'",
            "CENTER": "'500@399'", # Earth observer
            "START_TIME": f"'{start_time}'",
            "STOP_TIME": f"'{stop_time}'",
            "STEP_SIZE": "'1 d'",
            "QUANTITIES": "'19,20'", # Distance and range rate
            "CSV_FORMAT": "'YES'"
        }

        try:
            response = requests.get(self.horizons_url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                result_text = data.get("result", "")

                # Parse CSV data section
                start_idx = result_text.find("$$SOE")
                end_idx = result_text.find("$$EOE")

                if start_idx != -1 and end_idx != -1:
                    csv_data = result_text[start_idx + 5 : end_idx].strip()
                    lines = csv_data.split('\n')
                    if lines:
                        # Index 5 is 'delta' (distance from observer to target in AU)
                        parts = lines[0].split(',')
                        if len(parts) > 5:
                            delta_au = float(parts[5].strip())
                            delta_km = delta_au * 149597870.7 # Convert AU to km
                            return delta_km
            print(f"{Colors.WARNING}Failed to parse Horizons data for {name}.{Colors.ENDC}")
            return None
        except Exception as e:
            print(f"{Colors.FAIL}Error fetching Horizons data for {name}: {e}{Colors.ENDC}")
            return None

    def fetch_solar_system_data(self, body_id):
        """Fetches physical properties from Le Systeme Solaire API"""
        print(f"Fetching physical parameters for {body_id} from Le Systeme Solaire...")
        try:
            response = requests.get(f"{self.solar_system_url}{body_id}", timeout=10)
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"{Colors.FAIL}Error fetching Solar System data for {body_id}: {e}{Colors.ENDC}")
            return None

    def analiz(self):
        print(f"\n{Colors.HEADER}=== LIVE NASA DATA & BASE-11 QUANTUM INTEGRATION ==={Colors.ENDC}")

        # 1. Fetch live Moon distance
        moon_dist_km = self.fetch_horizons_data("301", "Moon")
        if moon_dist_km:
            print(f"Live Moon Distance: {moon_dist_km:,.2f} km")
            # Base-11 Resonance Check (Target: 363,000 km)
            target = 363000
            diff = abs(moon_dist_km - target)
            resonance = (1 - (diff / target)) * 100
            print(f"Target Resonance (363k Code): {resonance:.4f}% Match")

            # Hatay Latitude Lock Check
            hatay_lat = 36.3
            ratio = moon_dist_km / (hatay_lat * 1000)
            print(f"Hatay (36.3°) Fractal Lock Ratio: {ratio:.4f} (Ideal: 10.0)")

        # 2. Fetch live Sun distance
        sun_dist_km = self.fetch_horizons_data("10", "Sun")
        if sun_dist_km:
            print(f"\nLive Sun Distance: {sun_dist_km:,.2f} km")
            # Check AU code
            au_target = 149597870.7
            diff_au = abs(sun_dist_km - au_target)
            print(f"Deviation from standard AU: {diff_au:,.2f} km")

            # Code 149 Lock
            print(f"Space-Time Lock 149 Code Check: {'Pass' if str(int(sun_dist_km)).startswith('149') else 'Fail'}")

        # 3. Fetch Moon equatorial radius
        moon_data = self.fetch_solar_system_data("moon")
        if moon_data and "equaRadius" in moon_data:
            moon_radius = moon_data["equaRadius"]
            print(f"\nMoon Equatorial Radius: {moon_radius} km")
            moon_diameter = moon_radius * 2

            # 11/3 Ratio check
            earth_diameter = 12742
            ratio_em = earth_diameter / moon_diameter
            print(f"Earth/Moon Diameter Ratio: {ratio_em:.4f}")
            print(f"Target (Simule Year 3.63): {abs(ratio_em - 3.63):.4f} Deviation")

        # 4. Fetch Sun equatorial radius
        sun_data = self.fetch_solar_system_data("sun")
        if sun_data and "equaRadius" in sun_data:
            sun_radius = sun_data["equaRadius"]
            print(f"\nSun Equatorial Radius: {sun_radius} km")
            sun_diameter = sun_radius * 2

            # 108-109 Ratio check
            earth_diameter = 12742
            ratio_se = sun_diameter / earth_diameter
            print(f"Sun/Earth Diameter Ratio: {ratio_se:.4f}")
            print(f"Target (109 Code): {abs(ratio_se - 109.0):.4f} Deviation")

        print(f"\n{Colors.GREEN}✓ LIVE DATA INTEGRATION COMPLETE{Colors.ENDC}")
