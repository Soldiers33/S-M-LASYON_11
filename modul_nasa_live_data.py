import requests

class Modul_NASA_LiveData:
    def __init__(self):
        self.api_url = "https://api.le-systeme-solaire.net/rest/bodies/"
        self.timeout = 10

    def get_nasa_data(self, body="sun"):
        try:
            response = requests.get(f"{self.api_url}{body}", timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            # Fallback for authorization or connection errors
            print(f"  [NASA API WARN] Request failed: {e}. Using static fallback for {body}.")
            if body == "sun":
                return {'equaRadius': 696340, 'meanRadius': 695700, 'mass': {'massValue': 1.989, 'massExponent': 30}}
            elif body == "earth":
                return {'equaRadius': 6378.137, 'meanRadius': 6371.0, 'mass': {'massValue': 5.972, 'massExponent': 24}}
            elif body == "moon":
                return {'equaRadius': 1738.1, 'meanRadius': 1737.4, 'mass': {'massValue': 7.342, 'massExponent': 22}}
            else:
                return {}

    def analiz(self):
        print("\n\033[96m[NASA LIVE DATA MODULE]\033[0m")
        sun_data = self.get_nasa_data("sun")
        earth_data = self.get_nasa_data("earth")
        moon_data = self.get_nasa_data("moon")

        sun_radius = sun_data.get('equaRadius', 'N/A')
        earth_radius = earth_data.get('equaRadius', 'N/A')
        moon_radius = moon_data.get('equaRadius', 'N/A')

        print(f"  => Sun Equatorial Radius: {sun_radius} km")
        print(f"  => Earth Equatorial Radius: {earth_radius} km")
        print(f"  => Moon Equatorial Radius: {moon_radius} km")

        return {
            "sun": sun_data,
            "earth": earth_data,
            "moon": moon_data
        }

if __name__ == "__main__":
    module = Modul_NASA_LiveData()
    module.analiz()
