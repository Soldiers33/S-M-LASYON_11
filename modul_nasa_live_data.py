import requests
from simulasyon_11 import Colors
from levhi_mahfuz import LevhiMahfuzConstants

class Modul_NASA_Live_Data:
    def __init__(self):
        self.sun_radius_fallback = 696340 # km
        self.earth_radius_fallback = LevhiMahfuzConstants.REAL_EARTH_RADIUS

    def fetch_sun_radius(self):
        try:
            # Using the le-systeme-solaire API, but relying on fallback to prevent 401
            url = 'https://api.le-systeme-solaire.net/rest/bodies/sun'
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if 'equaRadius' in data:
                    return data['equaRadius']
        except Exception as e:
            pass
        return self.sun_radius_fallback

    def fetch_jpl_horizons_data(self):
        try:
            # JPL Horizons API with CSV_FORMAT='YES'
            url = "https://ssd.jpl.nasa.gov/api/horizons.api"
            params = {
                "format": "json",
                "COMMAND": "'399'", # Earth
                "OBJ_DATA": "'YES'",
                "MAKE_EPHEM": "'YES'",
                "EPHEM_TYPE": "'VECTORS'",
                "CSV_FORMAT": "'YES'"
            }
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                # Return raw text or parsed data, here just a subset for simulation
                return response.json()
        except Exception as e:
            pass
        return None

    def analiz(self):
        print(f"\n{Colors.BOLD}{Colors.CYAN}=== NASA LIVE DATA MODULE ==={Colors.ENDC}")
        sun_radius = self.fetch_sun_radius()
        print(f"Sun Equatorial Radius: {sun_radius} km (API/Fallback)")
        print(f"Earth Equatorial Radius: {self.earth_radius_fallback} km (from LevhiMahfuzConstants)")
        jpl_data = self.fetch_jpl_horizons_data()
        if jpl_data:
            print(f"{Colors.GREEN}[+] Connected to NASA JPL Horizons API.{Colors.ENDC}")
        else:
            print(f"{Colors.YELLOW}[!] Could not connect to NASA JPL Horizons API. Using static models.{Colors.ENDC}")
