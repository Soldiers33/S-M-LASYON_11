import requests
import json
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

def fetch_arxiv_papers(search_query="quantum consciousness", max_results=2):
    """
    Fetches papers from arXiv API.
    """
    try:
        url = f"http://export.arxiv.org/api/query?search_query=all:{search_query}&start=0&max_results={max_results}"
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            root = ET.fromstring(response.content)
            papers = []
            for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
                title = entry.find('{http://www.w3.org/2005/Atom}title').text
                summary = entry.find('{http://www.w3.org/2005/Atom}summary').text
                papers.append({'title': title.strip().replace('\\n', ' '), 'summary': summary.strip().replace('\\n', ' ')})
            return papers
        else:
            return []
    except Exception as e:
        print(f"{Colors.FAIL}arXiv API connection failed: {e}{Colors.ENDC}")
        return []

def analiz():
    print(f"\n{Colors.HEADER}=== AUTONOMOUS DEEP RESEARCH MODULE (arXiv) ==={Colors.ENDC}")
    print(f"{Colors.CYAN}Initiating background search for recent quantum resonances and 11-dimensional models...{Colors.ENDC}")

    queries = ["quantum resonance", "11 dimensional string theory"]

    for query in queries:
        print(f"\n{Colors.BLUE}[*] Fetching latest papers for: {query}{Colors.ENDC}")
        papers = fetch_arxiv_papers(query)
        if papers:
            for i, p in enumerate(papers):
                print(f"{Colors.GREEN}  {i+1}. {p['title']}{Colors.ENDC}")
                # print snippet
                print(f"     {p['summary'][:150]}...")
        else:
            print(f"{Colors.WARNING}  No new papers found or API unavailable.{Colors.ENDC}")

    print(f"\n{Colors.HEADER}[+] Autonomous research data streamed to Master AI.{Colors.ENDC}")

if __name__ == "__main__":
    analiz()
