import requests
import datetime

class Modul_Nasa_Live_Data:
    def __init__(self):
        self.base_url = "https://ssd.jpl.nasa.gov/api/horizons.api"

    def fetch_data(self, command_id):
        now = datetime.datetime.now(datetime.timezone.utc)
        stop_time = now + datetime.timedelta(days=1)

        params = {
            "format": "text",
            "COMMAND": f"'{command_id}'",
            "OBJ_DATA": "'YES'",
            "MAKE_EPHEM": "'YES'",
            "EPHEM_TYPE": "'OBSERVER'",
            "CENTER": "'500@399'", # Earth
            "START_TIME": f"'{now.strftime('%Y-%m-%d %H:%M')}'",
            "STOP_TIME": f"'{stop_time.strftime('%Y-%m-%d %H:%M')}'",
            "STEP_SIZE": "'1 d'",
            "QUANTITIES": "'19,20'",
            "CSV_FORMAT": "'YES'"
        }

        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()

            # Parse CSV
            data_started = False
            for line in response.text.splitlines():
                if line.strip() == "$$SOE":
                    data_started = True
                    continue
                if line.strip() == "$$EOE":
                    break

                if data_started:
                    parts = line.split(',')
                    if len(parts) > 5:
                        # Observer distance (delta) is at index 5 in the CSV output
                        try:
                            delta = float(parts[5].strip())
                            return delta
                        except ValueError:
                            pass

            return None
        except requests.exceptions.RequestException as e:
            print(f"NASA API Error: {e}")
            return None

    def get_sun_distance(self):
        # 10 is the ID for the Sun
        delta = self.fetch_data("10")
        if delta:
            # delta is in AU, convert to km
            return delta * 149597870.7
        return None

    def get_moon_distance(self):
        # 301 is the ID for the Moon
        delta = self.fetch_data("301")
        if delta:
            # delta is in AU, convert to km
            return delta * 149597870.7
        return None
