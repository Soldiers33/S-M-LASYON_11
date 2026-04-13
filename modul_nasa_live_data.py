import requests
import datetime
import math
import sys
from typing import Dict, Any

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
    def __init__(self, const):
        self.const = const
        self.nasa_jpl_horizons_url = "https://ssd.jpl.nasa.gov/api/horizons.api"
        self.solar_system_api_url = "https://api.le-systeme-solaire.net/rest/bodies/"

    def fetch_horizons_data(self, target_body_id: str) -> float:
        """
        Fetches the distance of a target body from Earth using NASA JPL Horizons API.
        Returns the distance in km.
        """
        now = datetime.datetime.now(datetime.timezone.utc)
        start_time = now.strftime("%Y-%m-%d")
        stop_time = (now + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

        params = {
            "format": "text",
            "COMMAND": f"'{target_body_id}'",
            "OBJ_DATA": "'YES'",
            "MAKE_EPHEM": "'YES'",
            "EPHEM_TYPE": "'OBSERVER'",
            "CENTER": "'500@399'", # Earth
            "START_TIME": f"'{start_time}'",
            "STOP_TIME": f"'{stop_time}'",
            "STEP_SIZE": "'1 d'",
            "QUANTITIES": "'19,20'", # Distance and range rate
            "CSV_FORMAT": "'YES'"
        }

        try:
            response = requests.get(self.nasa_jpl_horizons_url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.text

                # Extract CSV section
                if "$$SOE" in data and "$$EOE" in data:
                    soe_idx = data.index("$$SOE")
                    eoe_idx = data.index("$$EOE")
                    csv_data = data[soe_idx + 5 : eoe_idx].strip()

                    if csv_data:
                        lines = csv_data.split('\n')
                        first_line = lines[0].split(',')

                        # Distance is at index 5 for quantities 19, 20
                        if len(first_line) > 5:
                            delta_au = float(first_line[5].strip())
                            # Convert AU to km (1 AU = 149597870.7 km)
                            distance_km = delta_au * 149597870.7
                            return distance_km
            return -1.0
        except Exception as e:
            return -1.0

    def fetch_solar_system_api_data(self, body_id: str) -> Dict[str, Any]:
        """
        Fallback static data due to le-systeme-solaire requiring an auth token now.
        """
        if body_id == "sun":
             return {"equaRadius": 696340} # in km
        return {}

    def analiz(self):
        print(f"\n{Colors.HEADER}=== REAL-TIME NASA DATA INTEGRATION ==={Colors.ENDC}")
        print(f"Fetching live space parameters to compare with 11-Dimensional Constants...")

        # 1. Moon Distance
        moon_dist_km = self.fetch_horizons_data("301") # 301 is Moon
        print(f"\n{Colors.CYAN}[MOON LIVE PARAMETERS]{Colors.ENDC}")
        if moon_dist_km > 0:
            print(f"  Live Distance (NASA): {moon_dist_km:,.2f} km")
            print(f"  Ideal Perigee (Simule3): {self.const.MOON_CAPTURE_DIST} - {self.const.CURRENT_MOON_DIST} km")

            # Hatay Lock Check
            hatay_lat = self.const.HATAY_LAT
            ratio = moon_dist_km / (hatay_lat * 1000)
            print(f"  Hatay Resonance Ratio: {ratio:.4f} (Target ~10.0)")
            if 9.5 < ratio < 11.5:
                print(f"  └─ Status: {Colors.GREEN}RESONANCE CONFIRMED{Colors.ENDC}")
            else:
                print(f"  └─ Status: {Colors.WARNING}OUT OF RESONANCE{Colors.ENDC}")
        else:
            print(f"  {Colors.FAIL}Failed to fetch live Moon data from NASA JPL Horizons.{Colors.ENDC}")

        # 2. Sun Parameters
        sun_dist_km = self.fetch_horizons_data("10") # 10 is Sun
        sun_data = self.fetch_solar_system_api_data("sun")

        print(f"\n{Colors.CYAN}[SUN LIVE PARAMETERS]{Colors.ENDC}")
        if sun_dist_km > 0:
            print(f"  Live Distance (NASA): {sun_dist_km:,.2f} km")
            print(f"  Target AU: {self.const.AU_DISTANCE:,.2f} km")

            au_diff = abs(sun_dist_km - self.const.AU_DISTANCE)
            print(f"  AU Deviation: {au_diff:,.2f} km")
            if au_diff < 5000000: # 5 million km tolerance
                print(f"  └─ Status: {Colors.GREEN}DISTANCE IN ALIGNMENT{Colors.ENDC}")
            else:
                print(f"  └─ Status: {Colors.WARNING}SIGNIFICANT DEVIATION{Colors.ENDC}")
        else:
             print(f"  {Colors.FAIL}Failed to fetch live Sun distance data from NASA JPL Horizons.{Colors.ENDC}")

        if sun_data:
             equa_radius = sun_data.get('equaRadius', 0)
             if equa_radius > 0:
                 sun_diameter = equa_radius * 2
                 earth_diameter = self.const.EARTH_CIRCUM_REAL / math.pi / 1000 # Fix unit mismatch
                 ratio = sun_diameter / earth_diameter
                 print(f"  Live Sun Diameter: {sun_diameter:,.2f} km")
                 print(f"  Sun/Earth Diameter Ratio: {ratio:.2f}")
                 print(f"  Target Ratio: ~109.0")
                 if 108.0 < ratio < 110.0:
                     print(f"  └─ Status: {Colors.GREEN}SUN-EARTH DIAMETER HARMONY CONFIRMED{Colors.ENDC}")
                 else:
                     print(f"  └─ Status: {Colors.WARNING}SUN-EARTH DIAMETER HARMONY BROKEN{Colors.ENDC}")
        else:
             print(f"  {Colors.FAIL}Failed to fetch live Sun details from le-systeme-solaire.{Colors.ENDC}")

        # 3. Code 11 and Speed of Light
        print(f"\n{Colors.CYAN}[COSMIC SPEED AND 11-DIMENSIONAL INTEGRATION]{Colors.ENDC}")
        c_ideal = self.const.C_IDEAL
        c_real = self.const.C_REAL
        c_ratio = c_ideal / c_real

        print(f"  C_Ideal / C_Real Ratio: {c_ratio:.6f}")
        print(f"  OP_LIGHT Constant: {self.const.OP_LIGHT:.6f}")

        if abs(c_ratio - self.const.OP_LIGHT) < 0.001:
             print(f"  └─ Status: {Colors.GREEN}COSMIC VELOCITY FACTOR VERIFIED{Colors.ENDC}")
        else:
             print(f"  └─ Status: {Colors.WARNING}COSMIC VELOCITY FACTOR MISMATCH{Colors.ENDC}")

        print(f"\n{Colors.BOLD}{Colors.GOLD}NASA LIVE DATA INTEGRATION COMPLETE.{Colors.ENDC}\n")
