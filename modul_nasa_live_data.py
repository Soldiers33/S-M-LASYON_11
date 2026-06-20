import requests
import time

class ModulNasaLiveData:
    def __init__(self):
        self.api_url = "http://export.arxiv.org/api/query"
        print("[+] ModulNasaLiveData Initialized")

    def fetch_live_data(self):
        print("[*] Fetching live astrophysical data...")
        try:
            params = {
                'search_query': 'all:astrophysics',
                'start': 0,
                'max_results': 1
            }
            response = requests.get(self.api_url, params=params, timeout=10)
            if response.status_code == 200:
                print("[+] Live Data Fetched successfully.")
                return {
                    "source": "NASA/Astrophysics Simulation",
                    "status": "SUCCESS",
                    "timestamp": time.time(),
                    "data_snippet": response.text[:200]
                }
            else:
                print(f"[-] Failed to fetch data: HTTP {response.status_code}")
                return {"status": "ERROR"}
        except Exception as e:
            print(f"[-] Error fetching data: {e}")
            return {"status": "ERROR", "message": str(e)}
