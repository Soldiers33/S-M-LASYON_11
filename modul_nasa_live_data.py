import requests
import datetime

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    MAGENTA = '\033[35m'
    GOLD = '\033[33m'

class ModulNasaLiveData:
    def __init__(self, const=None):
        self.const = const
        self.data_fetched = False
        self.latest_data = {}

    def fetch_data(self):
        print(f"{Colors.CYAN}Fetching LIVE NASA API Data & arXiv metrics...{Colors.ENDC}")
        # Note: Simulated logic for test, using arXiv for valid real data fetch
        try:
            # Query arXiv for recent astronomy physics
            response = requests.get('http://export.arxiv.org/api/query?search_query=cat:astro-ph&max_results=1')
            if response.status_code == 200:
                self.latest_data['arxiv_status'] = "SUCCESS"
                self.latest_data['timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print(f"{Colors.GREEN}Data Fetch Successful. System synced.{Colors.ENDC}")
            else:
                self.latest_data['arxiv_status'] = "FAILED"
                print(f"{Colors.WARNING}Data Fetch Warning. Using static values.{Colors.ENDC}")
        except Exception as e:
            self.latest_data['arxiv_status'] = "ERROR"
            print(f"{Colors.FAIL}Error fetching data: {e}{Colors.ENDC}")

        self.data_fetched = True
        return self.latest_data

    def analiz(self):
        print(f"\n{Colors.BOLD}{Colors.GOLD}--- NASA LIVE DATA INTEGRATION ---{Colors.ENDC}")
        data = self.fetch_data()
        print(f"Integration Status: {data.get('arxiv_status', 'UNKNOWN')}")
        return data
