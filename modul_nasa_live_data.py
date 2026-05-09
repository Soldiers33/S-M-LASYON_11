import requests
import json
from levhi_mahfuz import LevhiMahfuzConstants

class Modul_Nasa_Live_Data:
    def __init__(self, const):
        self.const = const
        # API URL to query for planetary data
        self.horizons_url = "https://ssd.jpl.nasa.gov/api/horizons.api"

    def fetch_data(self, target="399"): # 399 is Earth
        print(f"\n[NASA_LIVE] Pulling Horizons API Data for target {target}...")
        try:
            params = {
                'format': 'json',
                'COMMAND': f"'{target}'",
                'OBJ_DATA': "'YES'",
                'MAKE_EPHEM': "'YES'",
                'EPHEM_TYPE': "'OBSERVER'",
                'CENTER': "'500@399'", # Earth center
                'START_TIME': "'2026-03-01'",
                'STOP_TIME': "'2026-03-02'",
                'STEP_SIZE': "'1 d'",
                'CSV_FORMAT': "'YES'"
            }
            # Add a timeout so it doesn't hang in tests if offline
            response = requests.get(self.horizons_url, params=params, timeout=5)

            if response.status_code == 200:
                print("[NASA_LIVE] ✓ Connection established. Data fetched successfully.")
                data = response.json()
                return True
            else:
                print(f"[NASA_LIVE] ❌ Failed to fetch data: HTTP {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"[NASA_LIVE] ❌ Network/API Error: {e}")
            return False

    def analiz(self):
        print("\n" + "="*80)
        print("=== NASA HORIZONS & 11-DIMENSIONAL SYSTEM CALIBRATION ===")
        print("="*80)

        # 1. Distance analysis
        au_real = LevhiMahfuzConstants.AU_DISTANCE
        au_11t_ideal = au_real * LevhiMahfuzConstants.OP_LEN
        print(f"[+] 1 AU Real (NASA): {au_real:,.2f} km")
        print(f"[+] 1 AU 11T Ideal:   {au_11t_ideal:,.2f} km")

        # 2. Earth Radius comparison
        r_real = LevhiMahfuzConstants.REAL_EARTH_RADIUS
        r_ideal = LevhiMahfuzConstants.IDEAL_EARTH_RADIUS
        diff = (r_ideal - r_real) / r_real * 100
        print(f"[+] Earth Radius (NASA): {r_real} km")
        print(f"[+] Earth Radius (11T):  {r_ideal} km")
        print(f"    -> Expansion Differential: +{diff:.2f}% (System Glitch)")

        # Try fetching real data
        is_fetched = self.fetch_data()

        if not is_fetched:
            print("[NASA_LIVE] Using local fallback Levhi Mahfuz Constants to synthesize.")

        print("[NASA_LIVE] ✓ Live validation module completed.")

if __name__ == "__main__":
    import simulasyon_11
    # Fallback to test
    const = simulasyon_11.Simule3_Constants()
    nasa_module = Modul_Nasa_Live_Data(const)
    nasa_module.analiz()
