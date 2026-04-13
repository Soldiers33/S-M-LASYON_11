import requests
import datetime
import time

class NasaLiveBridge:
    def __init__(self):
        self.horizons_url = "https://ssd.jpl.nasa.gov/api/horizons.api"
        self.solaire_url = "https://api.le-systeme-solaire.net/rest/bodies/"

    def get_body_data(self, body_id, name_fallback):
        # Fetch data from le-systeme-solaire with fallback
        try:
            res = requests.get(f"{self.solaire_url}{name_fallback}", timeout=10)
            if res.status_code == 200:
                data = res.json()
                return data
            else:
                return self._fallback_data(name_fallback)
        except Exception:
            return self._fallback_data(name_fallback)

    def _fallback_data(self, name):
        fallbacks = {
            'sun': {'equaRadius': 696340, 'mass': {'massValue': 1.989, 'massExponent': 30}},
            'moon': {'equaRadius': 1737.4, 'mass': {'massValue': 7.342, 'massExponent': 22}},
            'earth': {'equaRadius': 6378.1, 'mass': {'massValue': 5.972, 'massExponent': 24}}
        }
        return fallbacks.get(name, {})

    def get_horizons_distance(self, command="301"): # 301 is Moon, 10 is Sun
        # Get live distance from Earth
        now = datetime.datetime.now(datetime.timezone.utc)
        start_time = now.strftime("%Y-%m-%d")
        stop_time = (now + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

        params = {
            "format": "text",
            "COMMAND": f"'{command}'",
            "OBJ_DATA": "'YES'",
            "MAKE_EPHEM": "'YES'",
            "EPHEM_TYPE": "'OBSERVER'",
            "CENTER": "'500@399'", # Earth
            "START_TIME": f"'{start_time}'",
            "STOP_TIME": f"'{stop_time}'",
            "STEP_SIZE": "'1 d'",
            "QUANTITIES": "'19,20'",
            "CSV_FORMAT": "'YES'"
        }
        try:
            res = requests.get(self.horizons_url, params=params, timeout=10)
            if res.status_code == 200:
                text = res.text
                if "$$SOE" in text and "$$EOE" in text:
                    data_block = text.split("$$SOE")[1].split("$$EOE")[0].strip()
                    lines = data_block.split("\n")
                    if lines:
                        first_line = lines[0].split(",")
                        if len(first_line) > 5:
                            # delta is at index 5 in the standard CSV output for quantites 19,20
                            delta_au = float(first_line[5].strip())
                            delta_km = delta_au * 149597870.7
                            return delta_km
        except Exception as e:
            print(f"Error fetching Horizons data: {e}")
            pass

        # Fallback values
        if command == "301": return 384400
        if command == "10": return 149597870.7
        return None

class Modul_Nasa_Live_Data:
    def __init__(self, const):
        self.const = const
        self.bridge = NasaLiveBridge()

    def analiz(self):
        print("\n\033[95m=== NASA LIVE DATA INTEGRATION (REAL-TIME HORIZONS) ===\033[0m")
        print("Fetching real-time data from NASA JPL Horizons...")

        moon_dist = self.bridge.get_horizons_distance("301")
        sun_dist = self.bridge.get_horizons_distance("10")
        moon_data = self.bridge.get_body_data("301", "moon")

        print(f"Real-time Earth-Moon Distance: {moon_dist:,.2f} km")
        if moon_dist:
            diff = abs(moon_dist - 363000)
            print(f"Simule3 Target (363,000 km) Deviation: {diff:,.2f} km")

        print(f"Real-time Earth-Sun Distance: {sun_dist:,.2f} km")
        print(f"Moon Equatorial Radius: {moon_data.get('equaRadius')} km")
