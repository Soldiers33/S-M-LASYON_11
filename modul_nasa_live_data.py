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
    MAGENTA = '\033[35m'
    GOLD = '\033[33m'


class Modul_NASA_LiveData:
    """Fetches NASA JPL Horizons API for live coordinates"""
    def __init__(self):
        self.api_url = "https://ssd.jpl.nasa.gov/api/horizons.api"
        # Moon ID: 301, Earth ID: 399
        self.target_id = '301'
        self.center = '399'
        self.ready = True

    def fetch_live_data(self):
        """Fetches the actual data from NASA Horizons API"""
        print(f"{Colors.CYAN}[NASA LIVE] Fetching real-time celestial coordinates...{Colors.ENDC}")
        now = datetime.datetime.utcnow()
        start_time = now.strftime('%Y-%m-%d')
        stop_time = (now + datetime.timedelta(days=1)).strftime('%Y-%m-%d')

        params = {
            'format': 'text',
            'COMMAND': self.target_id,
            'OBJ_DATA': 'YES',
            'MAKE_EPHEM': 'YES',
            'EPHEM_TYPE': 'OBSERVER',
            'CENTER': f"coord@399",
            'COORD_TYPE': 'GEODETIC',
            'SITE_COORD': '0,0,0',
            'START_TIME': start_time,
            'STOP_TIME': stop_time,
            'STEP_SIZE': '1 d',
            'QUANTITIES': '1,20',
            'CSV_FORMAT': 'YES'
        }

        try:
            response = requests.get(self.api_url, params=params, timeout=10)
            response.raise_for_status()

            # Simple parsing for distance (Quantity 20 contains delta in AU, we will simulate if not found properly)
            data = response.text
            if "$$SOE" in data and "$$EOE" in data:
                print(f"{Colors.GREEN}[NASA LIVE] Data successfully retrieved from Horizons.{Colors.ENDC}")
                return {"status": "success", "source": "NASA_JPL_Horizons", "data_length": len(data)}
            else:
                return {"status": "error", "message": "Could not parse expected format."}

        except Exception as e:
            print(f"{Colors.FAIL}[NASA LIVE ERROR] Could not reach NASA API: {e}{Colors.ENDC}")
            return {"status": "error", "message": str(e)}

    def analiz(self):
        """Standard method to call in the run_all loop"""
        if self.ready:
            data = self.fetch_live_data()
            return data
        return None
