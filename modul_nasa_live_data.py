import requests
import datetime

class NASA_Live_Data_Module:
    def __init__(self):
        self.api_url = "https://ssd.jpl.nasa.gov/api/horizons.api"

    def fetch_data(self, command_id):
        now = datetime.datetime.now(datetime.timezone.utc)
        start_time = now.strftime("%Y-%m-%d")
        stop_time = (now + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

        params = {
            "format": "json",
            "COMMAND": f"'{command_id}'",
            "OBJ_DATA": "'YES'",
            "MAKE_EPHEM": "'YES'",
            "EPHEM_TYPE": "'OBSERVER'",
            "CENTER": "'500@399'",  # Earth
            "START_TIME": f"'{start_time}'",
            "STOP_TIME": f"'{stop_time}'",
            "STEP_SIZE": "'1 d'",
            "QUANTITIES": "'19,20'",
            "CSV_FORMAT": "'YES'"
        }

        try:
            response = requests.get(self.api_url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if "result" in data:
                    lines = data["result"].split('\n')
                    for i, line in enumerate(lines):
                        if "$$SOE" in line:
                            # The next line contains the CSV data
                            data_line = lines[i+1].split(',')
                            if len(data_line) > 5:
                                # Distance (delta) is usually at index 5 for quantities 19,20
                                distance_au = float(data_line[5].strip())
                                distance_km = distance_au * 149597870.7
                                return distance_km
            print(f"NASA API Call Failed or Data Not Found for {command_id}")
            return None
        except Exception as e:
            print(f"NASA API Exception for {command_id}: {e}")
            return None

    def get_moon_distance(self):
        # 301 is Moon
        return self.fetch_data('301')

    def get_sun_distance(self):
        # 10 is Sun
        return self.fetch_data('10')

    def analiz(self):
        print("\n=== NASA LIVE DATA SYNTHESIS ===")
        moon_dist = self.get_moon_distance()
        if moon_dist:
            print(f"Live Moon Distance from Earth: {moon_dist:,.2f} km")
            print(f"Deviation from Ideal (363,000 km): {abs(moon_dist - 363000):,.2f} km")
        else:
            print("Failed to fetch live Moon data.")

        sun_dist = self.get_sun_distance()
        if sun_dist:
            print(f"Live Sun Distance from Earth: {sun_dist:,.2f} km")
        else:
            print("Failed to fetch live Sun data.")
