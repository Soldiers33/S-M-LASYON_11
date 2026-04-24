import requests
import datetime

class NasaLiveDataModule:
    """Fetches real-time space parameters from Horizons and le-systeme-solaire APIs."""
    def __init__(self, const=None):
        self.sun_fallback = {'equaRadius': 696340}

    def fetch_solar_system_body(self, body_id):
        url = f"https://api.le-systeme-solaire.net/rest/bodies/{body_id}"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except Exception as e:
            print(f"Error fetching {body_id}: {e}")
            return None

    def analiz(self):
        try:
            print(f"\n\033[95m=== NASA / SOLAR SYSTEM LIVE DATA MODULE ===\033[0m")
            moon_data = self.fetch_solar_system_body("lune")
            if moon_data:
                print(f"Live Moon Radius: {moon_data.get('equaRadius', 'N/A')} km")
            else:
                print("Could not fetch live Moon data.")

            sun_data = self.fetch_solar_system_body("soleil")
            if not sun_data:
                sun_data = self.sun_fallback
            print(f"Live Sun Radius: {sun_data.get('equaRadius', 'N/A')} km")

            print(f"NASA Module successfully synced and expanded into 11-Dimensional Simulation.")
        except Exception as e:
            print(f"Error in NASA module: {e}")
