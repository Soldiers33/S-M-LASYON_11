import requests
import json
import datetime
import traceback

class Modul_NASA_Live_Data:
    def __init__(self, const):
        self.const = const
        # Primary API: le-systeme-solaire (public, no auth required for basic)
        self.solar_api_url = "https://api.le-systeme-solaire.net/rest/bodies/"
        # Fallback constants
        self.fallback_data = {
            "earth": {"equaRadius": 6378.137, "meanRadius": 6371.0},
            "sun": {"equaRadius": 696340, "meanRadius": 696340},
            "moon": {"equaRadius": 1738.1, "meanRadius": 1737.4}
        }

    def get_body_data(self, body_id):
        try:
            url = f"{self.solar_api_url}{body_id}"
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.json()
            else:
                return self.fallback_data.get(body_id, {})
        except Exception as e:
            return self.fallback_data.get(body_id, {})

    def analiz(self):
        print(f"\n\033[1m\033[96m=== NASA / SOLAR SYSTEM LIVE DATA MODULE ===\033[0m")
        try:
            earth_data = self.get_body_data("earth")
            sun_data = self.get_body_data("sun")
            moon_data = self.get_body_data("moon")

            earth_radius = earth_data.get("equaRadius", self.fallback_data["earth"]["equaRadius"])
            sun_radius = sun_data.get("equaRadius", self.fallback_data["sun"]["equaRadius"])
            moon_radius = moon_data.get("equaRadius", self.fallback_data["moon"]["equaRadius"])

            print(f"[\033[92mOK\033[0m] Retrieved live/fallback data.")
            print(f"    - Earth Equatorial Radius: {earth_radius} km")
            print(f"    - Sun Equatorial Radius: {sun_radius} km")
            print(f"    - Moon Equatorial Radius: {moon_radius} km")

            # Simple simulation correlation
            ideal_earth_radius = getattr(self.const, 'IDEAL_EARTH_RADIUS', 6666)
            print(f"    - Ideal Earth Radius (11-T Matrix): {ideal_earth_radius} km")
            if ideal_earth_radius != earth_radius:
                diff = abs(ideal_earth_radius - earth_radius)
                print(f"    - Glitch Deviation (Matrix Gap): {diff:.2f} km")

        except Exception as e:
            print(f"[\033[91mERROR\033[0m] NASA Module encountered an error: {e}")
            traceback.print_exc()

if __name__ == "__main__":
    class MockConst:
        IDEAL_EARTH_RADIUS = 6666
    Modul_NASA_Live_Data(MockConst()).analiz()
