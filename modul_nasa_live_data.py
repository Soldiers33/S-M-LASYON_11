import requests
import datetime
import math

class ModulNasaLiveData:
    def __init__(self, const):
        self.const = const
        self.api_url = "https://ssd.jpl.nasa.gov/api/horizons.api"

    def fetch_body_data(self, body_id):
        # NASA Horizons API request
        now = datetime.datetime.now(datetime.timezone.utc)
        start_time = now.strftime('%Y-%m-%d')
        end_time = (now + datetime.timedelta(days=1)).strftime('%Y-%m-%d')

        params = {
            "format": "text",
            "COMMAND": f"'{body_id}'",
            "OBJ_DATA": "'YES'",
            "MAKE_EPHEM": "'YES'",
            "EPHEM_TYPE": "'OBSERVER'",
            "CENTER": "'500@399'",  # Earth
            "START_TIME": f"'{start_time}'",
            "STOP_TIME": f"'{end_time}'",
            "STEP_SIZE": "'1 d'",
            "QUANTITIES": "'19,20'", # Distance and range rate
            "CSV_FORMAT": "'YES'"
        }

        try:
            response = requests.get(self.api_url, params=params, timeout=10)
            response.raise_for_status()

            # Simple parsing for distance (Delta)
            lines = response.text.split('\n')
            in_data = False
            for line in lines:
                if '$$SOE' in line:
                    in_data = True
                    continue
                if '$$EOE' in line:
                    break
                if in_data:
                    parts = line.split(',')
                    if len(parts) > 5:
                        delta_au = float(parts[5].strip()) # Observer distance in AU
                        delta_km = delta_au * 149597870.7
                        return delta_km
            return None
        except Exception as e:
            print(f"NASA API Error for body {body_id}: {e}")
            return None

    def analiz(self):
        print("\n\033[95m=== NASA LIVE DATA INTEGRATION ===\033[0m")
        # Body 301 is Moon, 10 is Sun
        moon_dist = self.fetch_body_data("301")
        if moon_dist:
            print(f"Live Moon Distance from Earth: {moon_dist:,.2f} km")
            if hasattr(self.const, 'IDEAL_MOON_PERIGEE'):
                print(f"Simulation Ideal Moon Perigee: {self.const.IDEAL_MOON_PERIGEE:,.2f} km")
                print(f"Deviation: {abs(moon_dist - self.const.IDEAL_MOON_PERIGEE):,.2f} km")
            elif hasattr(self.const, 'MOON_PERIGEE_IDEAL'):
                 print(f"Simulation Ideal Moon Perigee: {self.const.MOON_PERIGEE_IDEAL:,.2f} km")
                 print(f"Deviation: {abs(moon_dist - self.const.MOON_PERIGEE_IDEAL):,.2f} km")
        else:
            print("Could not fetch live Moon data.")

        sun_dist = self.fetch_body_data("10")
        if sun_dist:
            print(f"Live Sun Distance from Earth: {sun_dist:,.2f} km")
        else:
            print("Could not fetch live Sun data.")

        # Earth vs Sun diameter comparison
        earth_circum_real = getattr(self.const, 'EARTH_CIRCUM_REAL', 40007863)
        earth_diam_km = earth_circum_real / math.pi / 1000
        print(f"Earth Diameter (Calculated from Circumference): {earth_diam_km:,.2f} km")
        print(f"Sun Equatorial Radius (Static Fallback): 696340 km")
        print(f"Ratio Sun Radius to Earth Diameter: {696340 / earth_diam_km:.2f}")
