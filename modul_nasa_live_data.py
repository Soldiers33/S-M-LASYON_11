import requests
import datetime
import math
import sys

# Color constants
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

    def fetch_moon_distance(self):
        # Fetch Moon distance from Earth using NASA JPL Horizons API
        url = 'https://ssd.jpl.nasa.gov/api/horizons.api'
        now = datetime.datetime.now(datetime.timezone.utc)
        tomorrow = now + datetime.timedelta(days=1)
        params = {
            'format': 'json',
            'COMMAND': '"301"', # Moon
            'OBJ_DATA': '"YES"',
            'MAKE_EPHEM': '"YES"',
            'EPHEM_TYPE': '"OBSERVER"',
            'CENTER': '"500@399"', # Earth
            'START_TIME': f'"{now.strftime("%Y-%m-%d")}"',
            'STOP_TIME': f'"{tomorrow.strftime("%Y-%m-%d")}"',
            'STEP_SIZE': '"1 d"',
            'QUANTITIES': '"19,20"',
            'CSV_FORMAT': '"YES"'
        }
        try:
            resp = requests.get(url, params=params, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                result_text = data.get('result', '')

                # Parse CSV part
                csv_started = False
                for line in result_text.split('\n'):
                    if line.startswith('$$SOE'):
                        csv_started = True
                        continue
                    if line.startswith('$$EOE'):
                        break
                    if csv_started:
                        parts = [p.strip() for p in line.split(',')]
                        if len(parts) >= 6:
                            # Distance is typically in AU, at index 5 for quantities 19,20
                            # delta is at index 5 in the row: Date, , , r, rdot, delta, deldot,
                            delta_au = float(parts[5])
                            # Convert AU to km (using ideal symbolic AU or standard 149597870.7)
                            # Let's use standard AU for accurate km
                            dist_km = delta_au * 149597870.7
                            return dist_km
        except Exception as e:
            print(f"Error fetching NASA Moon data: {e}")
        return None

    def fetch_sun_radius(self):
        # Use le-systeme-solaire API as fallback for body sizes since Horizons is complex for that
        try:
            resp = requests.get('https://api.le-systeme-solaire.net/rest/bodies/sun', timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                return data.get('equaRadius')
        except:
            pass
        return None

    def analiz(self):
        print(f"\n{Colors.HEADER}=== NASA LIVE DATA INTEGRATION ==={Colors.ENDC}")
        print("Fetching real-time celestial data...")

        moon_dist_km = self.fetch_moon_distance()
        if moon_dist_km:
            print(f"Live Earth-Moon Distance: {moon_dist_km:,.2f} km")
            # Calculate resonance with 363
            resonance = moon_dist_km / 1000
            diff = abs(resonance - 363.0)
            print(f"Base-11 Code Resonance (Target 363.0): {resonance:,.2f}")
            print(f"Deviation from Ideal Perigee: {diff:,.2f} ({diff/363.0 * 100:.2f}%)")
        else:
            print("Could not fetch live Moon distance.")

if __name__ == '__main__':
    from simulasyon_11 import Simule3_Constants
    const = Simule3_Constants()
    mod = Modul_Nasa_Live_Data(const)
    mod.analiz()
