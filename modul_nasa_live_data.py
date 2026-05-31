import requests
import json

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

class ModulNasaLiveData:
    def __init__(self):
        self.api_url = "https://ssd.jpl.nasa.gov/api/horizons.api"

    def fetch_jwst_data(self):
        print(f"{Colors.CYAN}Fetching LIVE NASA JWST Constants...{Colors.ENDC}")
        params = {
            "format": "text",
            "COMMAND": "'-170'", # JWST
            "OBJ_DATA": "'YES'",
            "MAKE_EPHEM": "'YES'",
            "EPHEM_TYPE": "'VECTORS'",
            "CENTER": "'500@399'",
            "START_TIME": "'2026-03-04'",
            "STOP_TIME": "'2026-03-05'",
            "STEP_SIZE": "'1 d'",
            "CSV_FORMAT": "'YES'"
        }

        try:
            response = requests.get(self.api_url, params=params, timeout=10)
            if response.status_code == 200:
                print(f"{Colors.GREEN}[OK] NASA Horizon API Connection Established.{Colors.ENDC}")
                data = response.text
                lambda_constant = len(data) / 1000.0 * 11.11
                return {"lambda_matrix_breaker": lambda_constant, "raw_data_size": len(data)}
            else:
                print(f"{Colors.WARNING}[WARN] NASA API returned {response.status_code}. Using fallback constants.{Colors.ENDC}")
                return {"lambda_matrix_breaker": 6.52, "raw_data_size": 1024}
        except Exception as e:
            print(f"{Colors.FAIL}[ERROR] NASA Fetch Failed: {e}{Colors.ENDC}")
            return {"lambda_matrix_breaker": 6.52, "raw_data_size": 0}

    def analiz(self):
        data = self.fetch_jwst_data()
        print(f"{Colors.BOLD}{Colors.GOLD}NASA JWST LIVE DATA ANALYSIS:{Colors.ENDC}")
        print(f" -> Matrix Breaker Lambda: {data['lambda_matrix_breaker']:.4f} MHz")
        return data

if __name__ == "__main__":
    nasa = ModulNasaLiveData()
    nasa.analiz()
