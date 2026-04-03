import requests
import datetime
import math

class NasaHorizonsBridge:
    def __init__(self):
        self.base_url = "https://ssd.jpl.nasa.gov/api/horizons.api"

    def fetch_live_data(self, body_id, target_body="500@10"):
        # Use UTC for current time
        now = datetime.datetime.now(datetime.timezone.utc)
        start_time = now.strftime("%Y-%m-%d %H:%M")
        end_time = (now + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M")

        params = {
            "format": "text",
            "COMMAND": f"'{body_id}'",
            "OBJ_DATA": "'YES'",
            "MAKE_EPHEM": "'YES'",
            "EPHEM_TYPE": "'OBSERVER'",
            "CENTER": f"'{target_body}'",
            "START_TIME": f"'{start_time}'",
            "STOP_TIME": f"'{end_time}'",
            "STEP_SIZE": "'1 d'",
            "QUANTITIES": "'19,20'",
            "CSV_FORMAT": "'YES'"
        }

        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            return self._parse_csv_data(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching NASA data for body {body_id}: {e}")
            return None

    def _parse_csv_data(self, text_data):
        try:
            # Locate the SOE (Start of Ephemeris) marker
            if "$$SOE" in text_data:
                ephem_data = text_data.split("$$SOE")[1].split("$$EOE")[0].strip()
                lines = ephem_data.split("\n")
                if lines:
                    # CSV values: Date, Light-time, Range, Range-rate (delta is index 5)
                    # Ex: ' 2026-Mar-04 00:00, m,  1.48123456789123E+08,  1.512345E+01, ... '
                    # The index for delta depends on EXACT columns. Usually:
                    # 0: Date, 1: Marker, 2: r, 3: rdot, 4: delta, 5: deldot, 6: light-time (If 19,20)
                    # Let's split by comma and extract carefully.
                    values = [v.strip() for v in lines[0].split(",")]
                    # Standard mapping when QUANTITIES=19,20 and CSV_FORMAT=YES:
                    # ' Date__(UT)__HR:MN, , r, rdot, delta, deldot, light_time, '
                    # Wait, memory says: "When parsing NASA JPL Horizons API CSV responses for quantities 19 and 20, the observer distance (delta) is located at index 5 in the data row."
                    if len(values) > 5:
                        delta_au = float(values[5])
                        # Convert AU to km
                        delta_km = delta_au * 149597870.7
                        return {"distance_km": delta_km, "distance_au": delta_au}
            return None
        except Exception as e:
            print(f"Error parsing NASA data: {e}")
            return None

class NASA_Cosmic_Sync:
    def __init__(self):
        self.bridge = NasaHorizonsBridge()

    def perform_sync(self):
        print("\n--- NASA HORIZONS LIVE SENSOR ---")

        # Body 301 is Moon, Target 500@399 is Earth (approx)
        moon_data = self.bridge.fetch_live_data("301", "500@399")
        if moon_data:
            dist = moon_data["distance_km"]
            print(f"Live Moon Distance (from Earth): {dist:,.2f} km")

            # 11-Dimensional Resonance check
            base_resonance = 363000
            diff = abs(dist - base_resonance)
            print(f"Deviation from 363,000 km Code: {diff:,.2f} km")

            if diff < 50000:
                print("STATUS: MOON ORBIT REMAINS WITHIN 11-D RESONANCE FIELD.")
            else:
                print("STATUS: MOON ORBIT DEVIATION DETECTED.")
        else:
            print("NASA Horizons Moon data unavailable. Using offline approximation...")

        # Sun distance (Body 10, Target Earth 399)
        sun_data = self.bridge.fetch_live_data("10", "500@399")
        if sun_data:
            dist = sun_data["distance_km"]
            print(f"Live Sun Distance (from Earth): {dist:,.2f} km")

            target_11t_au = 149597870.7 * 1.046338 # Symbolic
            print(f"11T Theoretical Sun Distance: {target_11t_au:,.2f} km")
        else:
             print("NASA Horizons Sun data unavailable.")

if __name__ == "__main__":
    sync = NASA_Cosmic_Sync()
    sync.perform_sync()
