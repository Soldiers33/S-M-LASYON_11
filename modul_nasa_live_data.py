import requests
import json
import time
import math

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

class NASA_Live_Data_Module:
    def __init__(self):
        self.endpoint = "https://ssd.jpl.nasa.gov/api/horizons.api"
        # 11-Dimensional Reference Targets
        self.target_distance = 363000.0  # Moon Perigee Reference
        self.target_au = 149597870.7     # 1 AU Reference

    def fetch_moon_data(self):
        """Fetches live ephemeris data for the Moon from NASA JPL Horizons"""
        try:
            params = {
                "format": "json",
                "COMMAND": "'301'",     # Moon
                "OBJ_DATA": "'YES'",
                "MAKE_EPHEM": "'YES'",
                "EPHEM_TYPE": "'OBSERVER'",
                "CENTER": "'500@399'",  # Earth
                "START_TIME": time.strftime("%Y-%m-%d"),
                "STOP_TIME": time.strftime("%Y-%m-%d", time.localtime(time.time() + 86400)), # +1 day
                "STEP_SIZE": "'1 d'",
                "QUANTITIES": "'20'",   # Observer range & range-rate
                "CSV_FORMAT": "'YES'"
            }
            response = requests.get(self.endpoint, params=params, timeout=10)

            if response.status_code == 200:
                data = response.json()
                result_text = data.get("result", "")

                # Parse CSV section
                if "$$SOE" in result_text and "$$EOE" in result_text:
                    csv_data = result_text.split("$$SOE")[1].split("$$EOE")[0].strip()
                    lines = csv_data.split('\n')
                    if lines:
                        # Extract the first line's data (today)
                        fields = lines[0].split(',')
                        if len(fields) >= 4:
                            # Distance is typically in the 4th column (index 3) for QUANTITIES='20' in CSV format.
                            # Value is in km or AU, depending on JPL defaults, usually km for Earth-Moon.
                            # However, to be safe, we parse and fallback if it's too small (meaning it's in AU).
                            distance_val = float(fields[3].strip())
                            if distance_val < 1000:
                                distance_val = distance_val * self.target_au # Convert AU to km
                            return distance_val

            return None

        except Exception as e:
            # If the API fails, return a simulated close value based on simulation core
            return None

    def analiz(self):
        print(f"\n{Colors.HEADER}=== NASA JPL HORIZONS: LIVE DATA INTEGRATION ==={Colors.ENDC}")
        print(f"{Colors.CYAN}Connecting to NASA JPL API...{Colors.ENDC}")

        live_distance = self.fetch_moon_data()

        if live_distance:
            print(f"{Colors.GREEN}[+] Live Earth-Moon Distance Retrieved: {live_distance:,.2f} km{Colors.ENDC}")

            # Analyze 11-Dimensional Resonance
            deviation = abs(live_distance - self.target_distance)
            percentage = (deviation / self.target_distance) * 100

            print(f"{Colors.GOLD}--- 11-Dimensional Resonance Analysis ---{Colors.ENDC}")
            print(f"Target Perigee (Simule3): {self.target_distance:,.2f} km")
            print(f"Current Deviation: {deviation:,.2f} km ({percentage:.4f}%)")

            # 36.3 Hatay Lock verification
            lock_ratio = live_distance / 10000.0
            print(f"Live Hatay Fractal Lock: {lock_ratio:.4f} (Target: 36.3000)")

            if abs(lock_ratio - 36.3) < 5.0: # If within 5 degrees
                print(f"{Colors.GREEN}STATUS: MOON REMAINS WITHIN 11-DIMENSIONAL PARAMETERS.{Colors.ENDC}")
            else:
                print(f"{Colors.WARNING}STATUS: MOON DEVIATING FROM BASE ORBIT. AWAITING ALIGNMENT.{Colors.ENDC}")
        else:
            print(f"{Colors.FAIL}[-] NASA API Connection Failed or Data Unavailable.{Colors.ENDC}")
            print("Simulating local buffer...")
            sim_distance = 384400.0 # Average
            print(f"{Colors.CYAN}Local Buffer Earth-Moon Distance: {sim_distance:,.2f} km{Colors.ENDC}")
            print(f"Local Hatay Fractal Lock: {(sim_distance/10000.0):.4f} (Target: 36.3000)")

if __name__ == "__main__":
    module = NASA_Live_Data_Module()
    module.analiz()
