import requests
import datetime
from levhi_mahfuz import LevhiMahfuzConstants

class Modul_NASA_Live_Data:
    """
    Fetches real-time planetary parameters from NASA Horizons API
    and compares them to Base-11 constants.
    """
    def __init__(self):
        self.base_url = "https://ssd.jpl.nasa.gov/api/horizons.api"
        # Moon body id = 301, Earth body id = 399, Sun body id = 10
        self.timeout = 10 # Adding timeout to prevent hanging

    def _fetch_distance(self, target_id, observer_id='399'):
        """Fetches distance using quantities 19,20 (delta is index 5 in the CSV row)."""
        now = datetime.datetime.now(datetime.timezone.utc)
        start_time = now.strftime("%Y-%m-%d")
        stop_time = (now + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

        url = f"{self.base_url}?format=text&COMMAND='{target_id}'&OBJ_DATA='YES'&MAKE_EPHEM='YES'&EPHEM_TYPE='OBSERVER'&CENTER='500@{observer_id}'&START_TIME='{start_time}'&STOP_TIME='{stop_time}'&STEP_SIZE='1 d'&QUANTITIES='19,20'&CSV_FORMAT='YES'"

        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.text

            # Parse CSV response. The structure usually has $$SOE and $$EOE markers.
            if "$$SOE" in data and "$$EOE" in data:
                soe_index = data.find("$$SOE")
                eoe_index = data.find("$$EOE")
                csv_data = data[soe_index+6:eoe_index].strip().split('\n')
                if csv_data:
                    first_row = csv_data[0].split(',')
                    # The delta (distance from observer to target) is at index 5 in quantities 19,20.
                    if len(first_row) > 5:
                        delta_au = float(first_row[5].strip())
                        # Convert AU to km
                        return delta_au * 149597870.7
        except Exception as e:
            print(f"Error fetching data from NASA Horizons: {e}")
            pass
        return None

    def get_moon_distance(self):
        return self._fetch_distance('301')

    def get_sun_distance(self):
        return self._fetch_distance('10')

    def analiz(self):
        from simulasyon_11 import Colors
        print(f"\n{Colors.HEADER}=== NASA HORIZONS LIVE DATA INTEGRATION ==={Colors.ENDC}")

        moon_dist = self.get_moon_distance()
        if moon_dist:
            print(f"Live Moon Distance (NASA): {moon_dist:,.2f} km")
            print(f"Simule3 Ideal Perigee: {LevhiMahfuzConstants.IDEAL_MOON_PERIGEE:,.2f} km")
            diff = abs(moon_dist - LevhiMahfuzConstants.IDEAL_MOON_PERIGEE)
            print(f"Difference from Ideal: {diff:,.2f} km")
        else:
             print("Could not fetch Moon distance.")

        sun_dist = self.get_sun_distance()
        if sun_dist:
            print(f"Live Sun Distance (NASA): {sun_dist:,.2f} km")
            print(f"Simule3 Ideal AU: {LevhiMahfuzConstants.AU_DISTANCE:,.2f} km")
            diff = abs(sun_dist - LevhiMahfuzConstants.AU_DISTANCE)
            print(f"Difference from Ideal: {diff:,.2f} km")
        else:
             print("Could not fetch Sun distance.")
