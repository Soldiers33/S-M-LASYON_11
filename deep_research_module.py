import requests
import xml.etree.ElementTree as ET

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

class Deep_Research_Module:
    def __init__(self):
        # ArXiv API URL
        self.arxiv_url = "http://export.arxiv.org/api/query"
        self.search_query = "all:\"11 dimensions\" OR all:\"quantum gravity\""

    def analiz(self):
        print(f"\n{Colors.BOLD}{Colors.MAGENTA}--- INITIATING DEEP RESEARCH MODULE (arXiv) ---{Colors.ENDC}")
        try:
            params = {
                "search_query": self.search_query,
                "start": 0,
                "max_results": 3,
                "sortBy": "submittedDate",
                "sortOrder": "descending"
            }
            response = requests.get(self.arxiv_url, params=params, timeout=10)

            if response.status_code == 200:
                print(f"{Colors.GREEN}[+] arXiv API Connection Established.{Colors.ENDC}")
                root = ET.fromstring(response.content)

                ns = {'atom': 'http://www.w3.org/2005/Atom'}
                entries = root.findall('atom:entry', ns)

                if entries:
                    print(f"{Colors.BLUE}[*] Latest Research Findings on 11D/Quantum Gravity:{Colors.ENDC}")
                    for idx, entry in enumerate(entries):
                        title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
                        published = entry.find('atom:published', ns).text[:10]
                        print(f"  {Colors.GOLD}{idx+1}. [{published}] {title}{Colors.ENDC}")
                else:
                    print(f"{Colors.WARNING}[!] No recent matches found for 11 dimensions.{Colors.ENDC}")
            else:
                print(f"{Colors.WARNING}[!] arXiv API Unavailable (Status {response.status_code}).{Colors.ENDC}")

        except Exception as e:
            print(f"{Colors.FAIL}[X] Deep Research Module Error: {str(e)}{Colors.ENDC}")

        print(f"{Colors.MAGENTA}--- DEEP RESEARCH SYNC COMPLETE ---{Colors.ENDC}")

if __name__ == '__main__':
    research = Deep_Research_Module()
    research.analiz()
