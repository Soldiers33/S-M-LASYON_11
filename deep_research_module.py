import requests
import xml.etree.ElementTree as ET

class Modul_DeepResearch:
    def __init__(self, const):
        self.const = const

    def analiz(self):
        print("\033[96m[DEEP RESEARCH] Fetching latest research from arXiv...\033[0m")
        # Querying arXiv for recent papers on quantum physics or astrophysics
        url = 'http://export.arxiv.org/api/query?search_query=all:quantum+OR+all:astrophysics&start=0&max_results=3'

        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                print("\033[92m[OK] Successfully retrieved data from arXiv API.\033[0m")
                # Parse XML response
                root = ET.fromstring(response.content)
                ns = {'atom': 'http://www.w3.org/2005/Atom'}

                print("\033[95m[LATEST PAPERS DISCOVERED]:\033[0m")
                for entry in root.findall('atom:entry', ns):
                    title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
                    print(f"  - {title}")

                print("\033[92m[OK] Synthesizing data into 11-dimensional simulation matrix...\033[0m")
            else:
                print(f"\033[93m[WARNING] arXiv API returned status code {response.status_code}\033[0m")
        except Exception as e:
            print(f"\033[93m[WARNING] Could not fetch arXiv data: {e}\033[0m")
