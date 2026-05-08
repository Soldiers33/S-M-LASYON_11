import requests
import xml.etree.ElementTree as ET

class Deep_Research_Module:
    """Fetches recent research from arXiv to feed the 11-dimensional simulation."""
    def __init__(self):
        self.api_url = "http://export.arxiv.org/api/query"

    def fetch_recent_papers(self, search_query, max_results=3):
        try:
            params = {
                'search_query': f'all:{search_query}',
                'start': 0,
                'max_results': max_results,
                'sortBy': 'submittedDate',
                'sortOrder': 'descending'
            }
            response = requests.get(self.api_url, params=params, timeout=10)
            if response.status_code == 200:
                root = ET.fromstring(response.content)
                papers = []
                for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
                    title = entry.find('{http://www.w3.org/2005/Atom}title').text.strip()
                    papers.append(title)
                return True, papers
            return False, f"HTTP Error {response.status_code}"
        except Exception as e:
            return False, str(e)

    def analiz(self):
        print("Initializing Deep Research Module...")
        queries = ["quantum mechanics", "ancient history"]

        for query in queries:
            print(f"[*] Querying arXiv for: '{query}'...")
            success, results = self.fetch_recent_papers(query, max_results=2)
            if success:
                print(f"[+] Successfully fetched {len(results)} papers.")
                for title in results:
                    # Replacing newlines to prevent weird terminal outputs
                    clean_title = title.replace('\n', ' ').strip()
                    print(f"    -> {clean_title}")
            else:
                print(f"[-] Failed to fetch for '{query}': {results}")

        print("[+] Deep Research synchronization complete.")
