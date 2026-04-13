from modul_nasa_live_data import Modul_Nasa_Live_Data
from levhi_mahfuz import LevhiMahfuzConstants

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class Modul_Antik_Kuantum:
    def __init__(self):
        self.nasa = Modul_Nasa_Live_Data()

    def analiz(self):
        print(f"\n{Colors.HEADER}=== ANTIQUITY AND QUANTUM SYNTHESIS WITH LIVE NASA DATA ==={Colors.ENDC}")

        sun_dist = self.nasa.get_sun_distance()
        moon_dist = self.nasa.get_moon_distance()

        if sun_dist is None or moon_dist is None:
            print(f"{Colors.FAIL}Could not fetch live data from NASA API.{Colors.ENDC}")
            return

        print(f"Live Sun Distance: {sun_dist:,.2f} km")
        print(f"Live Moon Distance: {moon_dist:,.2f} km")

        # Antiquity synthesis
        giza_lat = LevhiMahfuzConstants.GIZA_LATITUDE
        # E.g. what is the ratio of sun distance to the giza latitude?
        giza_sun_ratio = sun_dist / giza_lat
        print(f"Giza Latitude: {giza_lat}")
        print(f"Sun Distance / Giza Latitude: {giza_sun_ratio:,.2f}")

        # Quantum synthesis
        vopson_k = LevhiMahfuzConstants.VOPSON_CONSTANT
        # Calculate something arbitrary for synthesis to show connection
        # E.g. Vopson constant applied to the moon distance
        quantum_moon_weight = moon_dist * 1000 * vopson_k # Convert km to m
        print(f"Vopson Information Constant: {vopson_k} kg/bit")
        print(f"Quantum 'Weight' of Moon Distance (m * Vopson_K): {quantum_moon_weight:e}")

        # Base-11 Synthesis
        print(f"Moon distance divided by 11: {moon_dist / 11:,.2f} km")

        print(f"{Colors.GREEN}Synthesis Complete.{Colors.ENDC}")
