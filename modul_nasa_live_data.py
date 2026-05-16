import requests
import datetime
import time

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def fetch_nasa_jpl_horizons(target_id='301', center='500@399'):
    """
    Fetches ephemeris data from NASA JPL Horizons.
    target_id: '301' for Moon
    center: '500@399' for Earth
    """
    try:
        url = "https://ssd.jpl.nasa.gov/api/horizons.api"
        # Request basic CSV format data for today
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        tomorrow = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

        params = {
            "format": "text",
            "COMMAND": f"'{target_id}'",
            "OBJ_DATA": "YES",
            "MAKE_EPHEM": "YES",
            "EPHEM_TYPE": "VECTORS",
            "CENTER": f"'{center}'",
            "START_TIME": f"'{today}'",
            "STOP_TIME": f"'{tomorrow}'",
            "STEP_SIZE": "'1 d'",
            "CSV_FORMAT": "YES"
        }

        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            return response.text
        else:
            return None
    except Exception as e:
        print(f"{Colors.FAIL}NASA JPL API connection failed: {e}{Colors.ENDC}")
        return None

def analiz():
    print(f"\n{Colors.HEADER}=== NASA JPL HORIZONS LIVE INTEGRATION ==={Colors.ENDC}")
    print(f"{Colors.CYAN}Querying live coordinates from NASA JPL Horizons API...{Colors.ENDC}")

    data = fetch_nasa_jpl_horizons(target_id='301') # Moon

    if data:
        # Extract X, Y, Z coordinates roughly from CSV block if it exists
        start_idx = data.find('$$SOE')
        end_idx = data.find('$$EOE')

        if start_idx != -1 and end_idx != -1:
            csv_data = data[start_idx+6:end_idx].strip()
            lines = csv_data.split('\n')
            if lines:
                parts = lines[0].split(',')
                if len(parts) >= 5:
                    x, y, z = parts[2].strip(), parts[3].strip(), parts[4].strip()
                    print(f"{Colors.GREEN}[+] Moon Coordinates (Relative to Earth){Colors.ENDC}")
                    print(f"    X: {x} km")
                    print(f"    Y: {y} km")
                    print(f"    Z: {z} km")
                    print(f"{Colors.WARNING}Live Data synchronized with Simulation Engine.{Colors.ENDC}")
                    return
        print(f"{Colors.WARNING}[!] API returned data, but CSV coordinates could not be parsed.{Colors.ENDC}")
    else:
        print(f"{Colors.FAIL}[!] Failed to fetch data from NASA JPL Horizons API.{Colors.ENDC}")

if __name__ == "__main__":
    analiz()
