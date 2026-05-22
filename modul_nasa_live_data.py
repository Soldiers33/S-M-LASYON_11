import requests
import datetime
import math
import io
try:
    import pandas as pd
except ImportError:
    pd = None

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
    MAGENTA = '\033[35m'
    PURPLE = '\033[35m'

class NASA_Live_Data_Module:
    """
    Connects to NASA JPL Horizons API to fetch live data
    and calculates 11-dimensional resonances based on
    Levh-i Mahfuz Constants.
    """
    def __init__(self):
        self.api_url = "https://ssd.jpl.nasa.gov/api/horizons.api"
        # 11-dimensional scaling factor
        self.scale_11 = 11.1111111111
        # Giza verification constant
        self.giza_verify = 11.08831

    def fetch_moon_data(self):
        """Fetches live Moon position data from NASA Horizons API"""
        print(f"\n{Colors.HEADER}=== NASA JPL HORIZONS API INTEGRATION ==={Colors.ENDC}")
        print(f"{Colors.CYAN}Initiating connection to NASA servers...{Colors.ENDC}")

        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)

        params = {
            "format": "text",
            "COMMAND": "'301'", # Moon
            "OBJ_DATA": "'YES'",
            "MAKE_EPHEM": "'YES'",
            "EPHEM_TYPE": "'OBSERVER'",
            "CENTER": "'500@399'", # Earth
            "START_TIME": f"'{today.strftime('%Y-%m-%d')}'",
            "STOP_TIME": f"'{tomorrow.strftime('%Y-%m-%d')}'",
            "STEP_SIZE": "'1 d'",
            "CSV_FORMAT": "'YES'"
        }

        url_params = "&".join([f"{k}={v}" for k, v in params.items()])
        full_url = f"{self.api_url}?{url_params}"

        try:
            response = requests.get(full_url, timeout=15)
            if response.status_code == 200:
                print(f"{Colors.GREEN}[OK] Connection established. Data received.{Colors.ENDC}")
                return self.parse_horizons_data(response.text)
            else:
                print(f"{Colors.FAIL}[ERROR] NASA API returned status code {response.status_code}{Colors.ENDC}")
                return None
        except Exception as e:
            print(f"{Colors.FAIL}[ERROR] Connection failed: {e}{Colors.ENDC}")
            return None

    def parse_horizons_data(self, data_text):
        """Parses CSV output from NASA Horizons API"""
        try:
            # Extract CSV section
            start_idx = data_text.find("$$SOE")
            end_idx = data_text.find("$$EOE")

            if start_idx == -1 or end_idx == -1:
                print(f"{Colors.WARNING}Data format error. Using simulation fallbacks.{Colors.ENDC}")
                return self.get_fallback_data()

            csv_data = data_text[start_idx + 6:end_idx].strip()
            lines = csv_data.split('\n')
            if not lines:
                return self.get_fallback_data()

            # Parse first line of data
            # Format varies but usually contains distance (delta)
            cols = lines[0].split(',')

            # Simple heuristic: Look for delta (distance from observer)
            # which is usually around column 24 in default observer output
            # Just grab a numeric value that looks like distance (in AU)
            distance_au = 0.00257 # fallback

            for col in cols:
                try:
                    val = float(col.strip())
                    if 0.001 < val < 0.003: # Moon distance range in AU
                        distance_au = val
                        break
                except ValueError:
                    pass

            distance_km = distance_au * 149597870.7

            return {
                "distance_au": distance_au,
                "distance_km": distance_km,
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        except Exception as e:
            print(f"{Colors.FAIL}[ERROR] Parsing failed: {e}{Colors.ENDC}")
            return self.get_fallback_data()

    def get_fallback_data(self):
        """Returns standard values if API fails"""
        return {
            "distance_au": 0.002569,
            "distance_km": 384400.0,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    def calculate_resonances(self, moon_data):
        """Calculates base-11 dimensional resonances based on live data"""
        if not moon_data:
            return

        dist_km = moon_data['distance_km']

        # Calculate Base-11 Resonance
        # Ideal perigee in Simule3 is 363000
        ideal_perigee = 363000
        deviation = dist_km - ideal_perigee
        dev_percentage = (deviation / ideal_perigee) * 100

        # 11D frequency resonance
        freq_11d = (dist_km / self.scale_11) / ideal_perigee

        print(f"\n{Colors.HEADER}=== LIVE 11-DIMENSIONAL ANALYSIS ==={Colors.ENDC}")
        print(f"Timestamp: {moon_data['timestamp']}")
        print(f"Live Moon Distance: {dist_km:,.2f} km")
        print(f"Simule3 Target Distance (363 Code): {ideal_perigee:,.2f} km")
        print(f"Deviation from Ideal: {deviation:,.2f} km ({dev_percentage:.2f}%)")
        print(f"11D Frequency Resonance: {freq_11d:.6f}")

        # Hatay Connection
        hatay_lat = 36.3
        fractal_lock = dist_km / (hatay_lat * 1000)
        print(f"Hatay Fractal Lock (Target 10.x): {fractal_lock:.4f}")

        # Giza Verification (Integration with KAR TOPU V5)
        giza_resonance = dist_km / (29.9792458 * 1000)
        print(f"Giza Light Resonance: {giza_resonance:.4f}")

        # Final output
        if abs(dev_percentage) < 10.0:
            print(f"{Colors.GREEN}[✓] Data falls within standard error margin for Corrupt Base-10 Matrix.{Colors.ENDC}")
        else:
            print(f"{Colors.WARNING}[!] Significant anomaly detected in gravitational tensor.{Colors.ENDC}")

    def analiz(self):
        """Main execution function compatible with Simule3 run_all()"""
        data = self.fetch_moon_data()
        self.calculate_resonances(data)

if __name__ == "__main__":
    module = NASA_Live_Data_Module()
    module.analiz()
