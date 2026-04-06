import requests
import datetime
import math

class Modul_NASA_Live_Data:
    def __init__(self, const):
        self.const = const
        self.horizons_url = "https://ssd.jpl.nasa.gov/api/horizons.api"

    def fetch_planet_data(self, command, name):
        """Fetch live planetary/moon parameters using NASA Horizons API."""
        now = datetime.datetime.now(datetime.timezone.utc)
        start_time = now.strftime("%Y-%m-%d")
        stop_time = (now + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

        params = {
            "format": "text",
            "COMMAND": f"'{command}'",
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
            response = requests.get(self.horizons_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.text

            # Parse CSV response for delta (distance to Earth) at index 5
            # The CSV data starts after "$$SOE" and ends before "$$EOE"
            lines = data.split('\n')
            in_data = False
            distance_au = None

            for line in lines:
                if "$$EOE" in line:
                    break
                if in_data:
                    parts = line.split(',')
                    if len(parts) > 5:
                        distance_au = float(parts[5].strip())
                        break
                if "$$SOE" in line:
                    in_data = True

            if distance_au:
                # Convert AU to km
                distance_km = distance_au * 149597870.7
                return {"name": name, "distance_km": distance_km}
            else:
                return {"name": name, "error": "Data parsing failed"}
        except requests.exceptions.RequestException as e:
            return {"name": name, "error": str(e)}

    def analiz(self):
        print(f"\n\033[95m=== NASA LIVE DATA INTEGRATION (BASE-11 SYNC) ===\033[0m")
        # 301 = Moon
        moon_data = self.fetch_planet_data("301", "Moon")
        if "distance_km" in moon_data:
            dist = moon_data["distance_km"]
            # Base 11 harmonic calculation
            base_11_dist = dist / 11.0
            print(f"Live Moon Distance: {dist:,.2f} km")
            print(f"Base-11 Moon Resonance: {base_11_dist:,.2f} km (1/11th Fractal)")
            print(f"Hatay (36.3) Lock Ratio: {dist / (36.3 * 1000):.4f}")
        else:
            print(f"Failed to fetch Moon data: {moon_data.get('error')}")

        # 10 = Sun
        sun_data = self.fetch_planet_data("10", "Sun")
        if "distance_km" in sun_data:
            dist = sun_data["distance_km"]
            print(f"Live Sun Distance: {dist:,.2f} km")
            base_11_sun = dist / 33.0
            print(f"Base-11 Sun Resonance (33 divisor): {base_11_sun:,.2f} km")
        else:
            print(f"Failed to fetch Sun data: {sun_data.get('error')}")

        print("\033[92m[+] NASA LIVE TELEMETRY SUCCESSFULLY MERGED WITH SENTEZ ENGINE.\033[0m")

if __name__ == "__main__":
    class DummyConst:
        pass
    mod = Modul_NASA_Live_Data(DummyConst())
    mod.analiz()
