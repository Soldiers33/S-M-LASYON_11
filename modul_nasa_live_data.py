import requests
import datetime
import math

class NasaHorizonsAPI:
    """
    Fetches live data from the NASA JPL Horizons API.
    """
    BASE_URL = "https://ssd.jpl.nasa.gov/api/horizons.api"

    @staticmethod
    def fetch_distance_au(body_id):
        """
        Fetches the current distance of a celestial body from Earth in AU.
        body_id: '301' for Moon, '10' for Sun
        """
        now = datetime.datetime.now(datetime.timezone.utc)
        start_time = now.strftime("%Y-%m-%d %H:%M")

        # We only need one data point
        stop_time = (now + datetime.timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M")

        params = {
            "format": "text",
            "COMMAND": f"'{body_id}'",
            "OBJ_DATA": "'NO'",
            "MAKE_EPHEM": "'YES'",
            "EPHEM_TYPE": "'OBSERVER'",
            "CENTER": "'500@399'", # Earth center
            "START_TIME": f"'{start_time}'",
            "STOP_TIME": f"'{stop_time}'",
            "STEP_SIZE": "'1 m'",
            "QUANTITIES": "'20'", # 20: Range and range-rate
            "CSV_FORMAT": "'YES'"
        }

        try:
            response = requests.get(NasaHorizonsAPI.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.text

            # Parse the text response to find the distance
            lines = data.split("\n")
            in_data = False
            for line in lines:
                if line.startswith("$$SOE"):
                    in_data = True
                    continue
                if line.startswith("$$EOE"):
                    break
                if in_data:
                    parts = line.split(",")
                    if len(parts) >= 3:
                        delta_au = float(parts[2].strip())
                        return delta_au

            return None

        except Exception as e:
            # Silent fail for API errors during simulation to prevent crashes
            return None

class Modul_Nasa_Live_Data:
    def __init__(self, const, colors):
        self.const = const
        self.colors = colors

    def analiz(self):
        print(f"\n{self.colors.HEADER}=== NASA LIVE HORIZONS API INTEGRATION (QUANTUM RESONANCE) ==={self.colors.ENDC}")

        # 1 AU in km
        au_to_km = 149597870.7

        # Fetch Moon distance (body 301)
        moon_dist_au = NasaHorizonsAPI.fetch_distance_au('301')
        if moon_dist_au is not None:
            moon_dist_km = moon_dist_au * au_to_km
            target_moon = 363000
            diff_moon = abs(moon_dist_km - target_moon)
            percent_moon = (diff_moon / target_moon) * 100

            print(f"{self.colors.CYAN}[MOON (301) LIVE DATA]{self.colors.ENDC}")
            print(f"Current Distance: {moon_dist_km:,.2f} km")
            print(f"Base-11 Target: {target_moon:,.2f} km")
            print(f"Deviation from Ideal: {percent_moon:.4f}%")
            if percent_moon < 10.0:
                 print(f"{self.colors.GREEN}MOON IS WITHIN RESONANCE WINDOW.{self.colors.ENDC}")
            else:
                 print(f"{self.colors.WARNING}MOON OUTSIDE IMMEDIATE RESONANCE.{self.colors.ENDC}")
        else:
            print(f"{self.colors.FAIL}Failed to fetch live Moon data from NASA API.{self.colors.ENDC}")

        # Fetch Sun distance (body 10)
        sun_dist_au = NasaHorizonsAPI.fetch_distance_au('10')
        if sun_dist_au is not None:
            sun_dist_km = sun_dist_au * au_to_km
            # Base-11 Target: 1 AU (Simule Constant)
            target_sun = self.const.EARTH_SUN_DIST # 149600000
            diff_sun = abs(sun_dist_km - target_sun)
            percent_sun = (diff_sun / target_sun) * 100

            print(f"\n{self.colors.CYAN}[SUN (10) LIVE DATA]{self.colors.ENDC}")
            print(f"Current Distance: {sun_dist_km:,.2f} km")
            print(f"Base-11 Target: {target_sun:,.2f} km")
            print(f"Deviation from Ideal: {percent_sun:.4f}%")
            if percent_sun < 5.0:
                 print(f"{self.colors.GREEN}SUN IS WITHIN QUANTUM HARMONIC.{self.colors.ENDC}")
        else:
            print(f"{self.colors.FAIL}Failed to fetch live Sun data from NASA API.{self.colors.ENDC}")

        print(f"\n{self.colors.GOLD}>> LIVE ANTI-GRAVITY HARMONY CHECK COMPLETED <<{self.colors.ENDC}")
