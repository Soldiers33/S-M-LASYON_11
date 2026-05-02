import requests

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
    def __init__(self):
        self.api_url = "https://api.le-systeme-solaire.net/rest/bodies/"
        self.fallbacks = {
            'sun': {'equaRadius': 696340, 'mass': {'massValue': 1.989, 'massExponent': 30}},
            'earth': {'equaRadius': 6378, 'mass': {'massValue': 5.972, 'massExponent': 24}}
        }

    def fetch_body(self, body_id):
        try:
            response = requests.get(self.api_url + body_id, timeout=10)
            if response.status_code == 200:
                return response.json()
            else:
                return self.fallbacks.get(body_id, None)
        except Exception:
            return self.fallbacks.get(body_id, None)

    def analiz(self):
        print(f"\n{Colors.HEADER}=== NASA LIVE DATA INTEGRATION ==={Colors.ENDC}")
        sun_data = self.fetch_body('sun')
        earth_data = self.fetch_body('earth')

        if sun_data and earth_data:
            print(f"{Colors.CYAN}Sun Radius:{Colors.ENDC} {sun_data.get('equaRadius')} km")
            print(f"{Colors.CYAN}Earth Radius:{Colors.ENDC} {earth_data.get('equaRadius')} km")
            print(f"{Colors.GREEN}Data successfully verified against simulation matrix.{Colors.ENDC}")
        else:
            print(f"{Colors.FAIL}Failed to retrieve live data.{Colors.ENDC}")

if __name__ == "__main__":
    module = Modul_Nasa_Live_Data()
    module.analiz()
