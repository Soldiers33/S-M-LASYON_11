import requests
import json
import math

class Modul_Nasa_Live_Data:
    def __init__(self):
        self.horizons_url = "https://ssd.jpl.nasa.gov/api/horizons.api"
        self.solaire_url = "https://api.le-systeme-solaire.net/rest/bodies/"

    def _fetch_horizons_data(self, target="301", center="500@399"):
        # target=301 is Moon, center=500@399 is Earth
        params = {
            "format": "json",
            "COMMAND": f"'{target}'",
            "OBJ_DATA": "'YES'",
            "MAKE_EPHEM": "'YES'",
            "EPHEM_TYPE": "'OBSERVER'",
            "CENTER": f"'{center}'",
            "START_TIME": "'2026-03-02'",
            "STOP_TIME": "'2026-03-03'",
            "STEP_SIZE": "'1 d'",
            "CSV_FORMAT": "'YES'"
        }
        try:
            response = requests.get(self.horizons_url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data.get('result', '')
            return ""
        except Exception as e:
            return ""

    def _fetch_solaire_data(self, body="moon"):
        try:
            response = requests.get(f"{self.solaire_url}{body}", timeout=10)
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            return None

    def analiz(self):
        print("\n\033[96m=== [NASA LIVE DATA MODULE INITIALIZED] ===\033[0m")
        print("Fetching real-time astronomical parameters...")

        # Solaire Data
        moon_data = self._fetch_solaire_data("moon")
        earth_data = self._fetch_solaire_data("earth")
        sun_data = self._fetch_solaire_data("sun")

        if moon_data:
            moon_radius = moon_data.get('equaRadius', 1737.4)
            print(f"\033[92m[✓] MOON EQUATORIAL RADIUS:\033[0m {moon_radius} km")
        else:
            print("\033[93m[!] USING FALLBACK MOON RADIUS:\033[0m 1737.4 km")

        if sun_data:
            sun_radius = sun_data.get('equaRadius', 696340)
            print(f"\033[92m[✓] SUN EQUATORIAL RADIUS:\033[0m {sun_radius} km")
        else:
            print("\033[93m[!] USING FALLBACK SUN RADIUS:\033[0m 696340 km")

        # Horizons Data
        horizons_result = self._fetch_horizons_data()
        if horizons_result:
            print("\033[92m[✓] NASA HORIZONS MOON-EARTH EPHEMERIS FETCHED\033[0m")
        else:
            print("\033[93m[!] NASA HORIZONS EPHEMERIS FETCH FAILED\033[0m")

        print("\033[96m=== [NASA LIVE DATA MODULE COMPLETE] ===\033[0m\n")

if __name__ == "__main__":
    modul = Modul_Nasa_Live_Data()
    modul.analiz()
