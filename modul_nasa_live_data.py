import math
import requests
import datetime

# --- VISUAL INTERFACE COLORS ---
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
    PURPLE = '\033[35m'
    MAGENTA = '\033[35m'


class Modul_Nasa_Live_Data:
    def __init__(self, const):
        self.const = const

    def get_nasa_horizons_data(self, command_id):
        # command_id: 301 for moon, 10 for sun
        now = datetime.datetime.now(datetime.timezone.utc)
        start_time = now.strftime('%Y-%m-%d')
        end_time = (now + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        url = f"https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND='{command_id}'&OBJ_DATA='YES'&MAKE_EPHEM='YES'&EPHEM_TYPE='OBSERVER'&CENTER='500@399'&START_TIME='{start_time}'&STOP_TIME='{end_time}'&STEP_SIZE='1 d'&QUANTITIES='19,20'&CSV_FORMAT='YES'"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.text
        except requests.exceptions.RequestException as e:
            print(f"{Colors.FAIL}Error fetching NASA Horizons API for {command_id}: {e}{Colors.ENDC}")
        return None

    def get_le_systeme_solaire_data(self, body_id):
        url = f"https://api.le-systeme-solaire.net/rest/bodies/{body_id}"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.json()
        except requests.exceptions.RequestException as e:
            print(f"{Colors.FAIL}Error fetching le-systeme-solaire API for {body_id}: {e}{Colors.ENDC}")
        return None

    def analiz(self):
        print(f"\n{Colors.HEADER}=== NASA LIVE DATA INTEGRATION ==={Colors.ENDC}")

        # Moon Observer Distance
        moon_data_str = self.get_nasa_horizons_data('301')
        moon_dist = None
        if moon_data_str:
            lines = moon_data_str.split('\n')
            in_data = False
            for line in lines:
                if line.startswith('$$SOE'):
                    in_data = True
                    continue
                if line.startswith('$$EOE'):
                    in_data = False
                    break
                if in_data:
                    parts = line.split(',')
                    if len(parts) > 5:
                        try:
                            # Delta is at index 5 and represents Earth-Moon observer distance in AU
                            moon_dist_au = float(parts[5].strip())
                            moon_dist = moon_dist_au * self.const.AU_DISTANCE
                            break
                        except ValueError:
                            continue

        if moon_dist:
            print(f"Live Moon Distance: {moon_dist:,.0f} km")
            diff = abs(moon_dist - self.const.MOON_CAPTURE_DIST)
            print(f"Deviation from Capture Distance ({self.const.MOON_CAPTURE_DIST}): {diff:,.0f} km")

        # Sun Observer Distance
        sun_data_str = self.get_nasa_horizons_data('10')
        sun_dist = None
        if sun_data_str:
            lines = sun_data_str.split('\n')
            in_data = False
            for line in lines:
                if line.startswith('$$SOE'):
                    in_data = True
                    continue
                if line.startswith('$$EOE'):
                    in_data = False
                    break
                if in_data:
                    parts = line.split(',')
                    if len(parts) > 5:
                        try:
                            # Delta is at index 5 and represents Earth-Sun observer distance in AU
                            sun_dist_au = float(parts[5].strip())
                            sun_dist = sun_dist_au * self.const.AU_DISTANCE
                            break
                        except ValueError:
                            continue

        if sun_dist:
            print(f"Live Sun Distance: {sun_dist:,.0f} km")
            diff = abs(sun_dist - self.const.AU_DISTANCE)
            print(f"Deviation from 1 AU ({self.const.AU_DISTANCE}): {diff:,.0f} km")


        # Solar System Bodies Details
        moon_details = self.get_le_systeme_solaire_data('moon')
        if moon_details and 'equaRadius' in moon_details:
             moon_radius = moon_details['equaRadius']
             print(f"Live Moon Equatorial Radius: {moon_radius} km")

        sun_details = self.get_le_systeme_solaire_data('sun')
        if sun_details and 'equaRadius' in sun_details:
             sun_radius = sun_details['equaRadius']
             print(f"Live Sun Equatorial Radius: {sun_radius} km")
