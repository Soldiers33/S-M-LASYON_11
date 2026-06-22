import requests
import json
import xml.etree.ElementTree as ET
import time

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

class ModulNasaLiveData:
    def __init__(self, const=None):
        self.const = const
        self.data_store = {}

    def fetch_nasa_data(self):
        print(f"\n{Colors.BOLD}{Colors.BLUE}*** FETCHING LIVE ASTROPHYSICAL DATA ***{Colors.ENDC}")
        # We use arXiv API to simulate fetching NASA/Astrophysics live papers
        url = 'http://export.arxiv.org/api/query?search_query=all:universe+expansion&start=0&max_results=3'
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            root = ET.fromstring(response.content)

            entries = []
            for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
                title = entry.find('{http://www.w3.org/2005/Atom}title').text
                entries.append(title.strip())

            self.data_store['arxiv_papers'] = entries
            print(f"{Colors.GREEN}[+] Successfully fetched {len(entries)} recent papers.{Colors.ENDC}")
            for paper in entries:
                print(f"    - {paper[:60]}...")
            return entries
        except Exception as e:
            print(f"{Colors.FAIL}[!] Failed to fetch live data: {e}{Colors.ENDC}")
            return None

    def analyze(self):
        print(f"\n{Colors.CYAN}--- LIVE DATA ANALYSIS ---{Colors.ENDC}")
        data = self.fetch_nasa_data()
        if data:
            print(f"{Colors.GREEN}[+] Live data successfully integrated into the simulation matrix.{Colors.ENDC}")
        else:
            print(f"{Colors.WARNING}[-] Live data unavailable. Proceeding with static simulation parameters.{Colors.ENDC}")
        return data

if __name__ == '__main__':
    module = ModulNasaLiveData()
    module.analyze()
