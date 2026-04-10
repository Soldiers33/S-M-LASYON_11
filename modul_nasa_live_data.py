import requests
import datetime
import csv
import io

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    GOLD = '\033[33m'

class NasaLiveModule:
    """
    NASA Live Data Bridge: Connects to JPL Horizons and le-systeme-solaire
    to feed real-time coordinates into the 11-Dimensional Simulation Engine.
    """
    def __init__(self, const):
        self.const = const

    def get_horizons_data(self, target="301", center="500@399"):
        """
        Fetch data from NASA JPL Horizons.
        301 = Moon, 500@399 = Earth center.
        """
        print(f"{Colors.CYAN}Connecting to NASA JPL Horizons for live tracking...{Colors.ENDC}")
        # Use timezone-aware UTC datetime instead of utcnow()
        now = datetime.datetime.now(datetime.timezone.utc)
        start_time = now.strftime("%Y-%m-%d")
        end_time = (now + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

        url = "https://ssd.jpl.nasa.gov/api/horizons.api"
        params = {
            "format": "text",
            "COMMAND": f"'{target}'",
            "OBJ_DATA": "'YES'",
            "MAKE_EPHEM": "'YES'",
            "EPHEM_TYPE": "'OBSERVER'",
            "CENTER": f"'{center}'",
            "START_TIME": f"'{start_time}'",
            "STOP_TIME": f"'{end_time}'",
            "STEP_SIZE": "'1 d'",
            "QUANTITIES": "'19,20'",
            "CSV_FORMAT": "'YES'"
        }

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()

            data = response.text
            start_idx = data.find("$$SOE")
            end_idx = data.find("$$EOE")

            if start_idx != -1 and end_idx != -1:
                ephem_data = data[start_idx + 5:end_idx].strip()
                reader = csv.reader(io.StringIO(ephem_data))
                rows = list(reader)
                if rows and len(rows[0]) > 5:
                    delta_au = float(rows[0][5])
                    # Ensure we use valid constants
                    # Since EARTH_CIRCUM_REAL is not directly in some consts, we use fallback
                    delta_km = delta_au * getattr(self.const, "AU_DISTANCE", 149597870.7)
                    return delta_km

            return None
        except requests.exceptions.RequestException as e:
            print(f"{Colors.FAIL}NASA Horizons API error: {e}{Colors.ENDC}")
            return None

    def get_solar_system_body(self, body_id="sun"):
        """Fetch supplemental data from le-systeme-solaire with static fallback."""
        print(f"{Colors.CYAN}Fetching {body_id} parameters from solar system API...{Colors.ENDC}")
        url = f"https://api.le-systeme-solaire.net/rest/bodies/{body_id}"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 401:
                print(f"{Colors.WARNING}API 401 Unauthorized. Using static fallback.{Colors.ENDC}")
                if body_id == "sun":
                    return {'equaRadius': 696340, 'mass': {'massValue': 1.989, 'massExponent': 30}}
                elif body_id == "moon":
                    return {'equaRadius': 1737.4, 'mass': {'massValue': 7.342, 'massExponent': 22}}
                return None
            else:
                 response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"{Colors.FAIL}Solar System API error: {e}. Using static fallback.{Colors.ENDC}")
            if body_id == "sun":
                 return {'equaRadius': 696340, 'mass': {'massValue': 1.989, 'massExponent': 30}}
            elif body_id == "moon":
                 return {'equaRadius': 1737.4, 'mass': {'massValue': 7.342, 'massExponent': 22}}
            return None

    def analiz(self):
        print(f"\n{Colors.HEADER}=== NASA LIVE DATA INTEGRATION (REAL-TIME ORBITAL SYNC) ==={Colors.ENDC}")

        moon_dist = self.get_horizons_data(target="301")
        if moon_dist:
            print(f"{Colors.GREEN}Live Moon Distance: {moon_dist:,.2f} km{Colors.ENDC}")
            target_11_dist = getattr(self.const, "IDEAL_MOON_PERIGEE", 363000)
            diff = abs(moon_dist - target_11_dist)
            print(f"Difference from Base-11 Ideal (363,000 km): {diff:,.2f} km")
        else:
            print(f"{Colors.WARNING}Could not retrieve live moon distance.{Colors.ENDC}")

        sun_data = self.get_solar_system_body("sun")
        if sun_data:
            radius = sun_data.get("equaRadius")
            print(f"{Colors.GREEN}Live Sun Equatorial Radius: {radius:,.2f} km{Colors.ENDC}")
            diameter = radius * 2
            earth_target = getattr(self.const, "REAL_EARTH_RADIUS", 6371) * 2
            ratio = diameter / earth_target
            print(f"Sun/Earth Diameter Ratio: {ratio:,.2f} (Target: 109)")
        else:
            print(f"{Colors.WARNING}Could not retrieve live sun data.{Colors.ENDC}")
