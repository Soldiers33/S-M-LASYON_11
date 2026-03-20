import requests
import datetime
from levhi_mahfuz import LevhiMahfuzConstants

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class Modul_Nasa_Live_Data:
    def __init__(self, const):
        self.const = const
        self.api_url = "https://ssd.jpl.nasa.gov/api/horizons.api"

    def fetch_horizons_data(self, body_id, name):
        now = datetime.datetime.now(datetime.timezone.utc)
        start_time = now.strftime('%Y-%m-%d')
        stop_time = (now + datetime.timedelta(days=1)).strftime('%Y-%m-%d')

        params = {
            "format": "text",
            "COMMAND": f"'{body_id}'",
            "OBJ_DATA": "'YES'",
            "MAKE_EPHEM": "'YES'",
            "EPHEM_TYPE": "'OBSERVER'",
            "CENTER": "'500@399'",
            "START_TIME": f"'{start_time}'",
            "STOP_TIME": f"'{stop_time}'",
            "STEP_SIZE": "'1 d'",
            "QUANTITIES": "'19,20'",
            "CSV_FORMAT": "'YES'"
        }

        try:
            response = requests.get(self.api_url, params=params, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"{Colors.FAIL}Error fetching NASA data for {name}: {e}{Colors.ENDC}")
            return None

    def parse_distance(self, text_data):
        if not text_data:
            return None

        lines = text_data.split('\n')
        in_data = False
        for line in lines:
            if line.startswith('$$SOE'):
                in_data = True
                continue
            if line.startswith('$$EOE'):
                break
            if in_data:
                parts = line.split(',')
                # Date__(UT)__HR:MN, , ,               r,       rdot,             delta,     deldot,
                # 2026-Mar-20 00:00, , ,  0.993332747628,  0.7256301,  0.00247499221905, -0.0319294,
                # The distance from observer is `delta`, which is index 5
                if len(parts) >= 6:
                    try:
                        # delta is distance from observer to target in AU
                        dist_au = float(parts[5].strip())
                        return dist_au * 149597870.7 # Convert AU to km
                    except ValueError:
                        pass
        return None

    def fetch_moon_distance(self):
        # 301 is Moon
        data = self.fetch_horizons_data('301', 'Moon')
        return self.parse_distance(data)

    def fetch_sun_distance(self):
        # 10 is Sun
        data = self.fetch_horizons_data('10', 'Sun')
        return self.parse_distance(data)

    def analiz(self):
        print(f"\n{Colors.HEADER}=== NASA LIVE DATA INTEGRATION (BASE-11 SYNC) ==={Colors.ENDC}")

        print("Fetching live data from NASA JPL Horizons...")
        moon_dist_km = self.fetch_moon_distance()
        sun_dist_km = self.fetch_sun_distance()

        if moon_dist_km:
            print(f"Live Moon Distance: {moon_dist_km:,.2f} km")
            target_moon = 363000.0 # From LevhiMahfuzConstants.IDEAL_MOON_PERIGEE
            diff = abs(moon_dist_km - target_moon)
            percent = (diff / target_moon) * 100
            print(f"Base-11 Ideal Perigee: {target_moon:,.2f} km")
            print(f"Variance: {diff:,.2f} km ({percent:.2f}%)")
            if percent < 10:
                 print(f"{Colors.GREEN}Resonance established. Moon is within acceptable Base-11 harmonic range.{Colors.ENDC}")
        else:
            print(f"{Colors.WARNING}Could not parse live Moon data.{Colors.ENDC}")

        if sun_dist_km:
            print(f"\nLive Sun Distance: {sun_dist_km:,.2f} km")
            target_sun = 149597870.7 # From LevhiMahfuzConstants.AU_DISTANCE
            diff = abs(sun_dist_km - target_sun)
            percent = (diff / target_sun) * 100
            print(f"Base-11 Ideal AU: {target_sun:,.2f} km")
            print(f"Variance: {diff:,.2f} km ({percent:.2f}%)")
            if percent < 5:
                 print(f"{Colors.GREEN}Resonance established. Sun is within acceptable Base-11 harmonic range.{Colors.ENDC}")
        else:
            print(f"{Colors.WARNING}Could not parse live Sun data.{Colors.ENDC}")

if __name__ == '__main__':
    from levhi_mahfuz import LevhiMahfuzConstants
    const = LevhiMahfuzConstants()
    m = Modul_Nasa_Live_Data(const)
    m.analiz()
