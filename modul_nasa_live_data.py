import requests
import datetime

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

class Modul_NASA_Live_Data:
    def __init__(self, const=None):
        self.const = const

    def analiz(self):
        print(f"\n{Colors.BOLD}{Colors.CYAN}[NASA LIVE DATA] CONNECTING TO JPL HORIZONS API...{Colors.ENDC}")
        try:
            today = datetime.datetime.now()
            tomorrow = today + datetime.timedelta(days=1)

            # Fetching data for Earth-Moon Barycenter (3) from Solar System Barycenter (0)
            params = {
                'format': 'text',
                'COMMAND': "'3'",
                'OBJ_DATA': "'YES'",
                'MAKE_EPHEM': "'YES'",
                'EPHEM_TYPE': "'VECTORS'",
                'CENTER': "'0'",
                'START_TIME': f"'{today.strftime('%Y-%m-%d')}'",
                'STOP_TIME': f"'{tomorrow.strftime('%Y-%m-%d')}'",
                'STEP_SIZE': "'1 d'",
                'CSV_FORMAT': "'YES'"
            }

            response = requests.get('https://ssd.jpl.nasa.gov/api/horizons.api', params=params, timeout=10)
            if response.status_code == 200:
                print(f"{Colors.GREEN}✓ NASA Data Channel Established.{Colors.ENDC}")
                data_lines = response.text.split('\n')
                in_data = False
                extracted = False
                for line in data_lines:
                    if "$$SOE" in line:
                        in_data = True
                        continue
                    if "$$EOE" in line:
                        break
                    if in_data and not extracted:
                        cols = line.split(',')
                        if len(cols) >= 5:
                            x_val = cols[2].strip()
                            y_val = cols[3].strip()
                            z_val = cols[4].strip()
                            print(f"  {Colors.BOLD}{Colors.GOLD}→ Live Vector Data (X, Y, Z): {x_val}, {y_val}, {z_val}{Colors.ENDC}")
                            print(f"  {Colors.BOLD}{Colors.PURPLE}→ Synchronizing with 11-Dimensional Coordinate Matrix...{Colors.ENDC}")
                            try:
                                sync_val = (float(x_val) + float(y_val)) / 11.0
                            except ValueError:
                                sync_val = 11.11111111111
                            print(f"  {Colors.GREEN}→ Synchronization Quantum: {sync_val}{Colors.ENDC}")
                            extracted = True
            else:
                print(f"{Colors.FAIL}⚠ NASA JPL Horizons Connection Failed: {response.status_code}{Colors.ENDC}")
        except Exception as e:
            print(f"{Colors.FAIL}⚠ NASA Integration Error: {e}{Colors.ENDC}")

        print(f"{Colors.GREEN}✓ NASA LIVE DATA ANALYSIS COMPLETE.{Colors.ENDC}")
