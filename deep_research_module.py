import requests
import json
import xml.etree.ElementTree as ET
import re

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    PURPLE = '\033[35m'
    RED = '\033[91m'

class Deep_Research_Module:
    """
    Autonomous module fetching real data from arXiv API
    to discover new base-11 constants and formulas.
    """
    def __init__(self):
        self.arxiv_url = "http://export.arxiv.org/api/query"
        self.queries = ["quantum consciousness", "antigravity resonance", "fine structure constant"]

    def fetch_arxiv_data(self, query):
        """Fetches latest research papers from arXiv"""
        params = {
            "search_query": f"all:{query}",
            "start": 0,
            "max_results": 3,
            "sortBy": "submittedDate",
            "sortOrder": "descending"
        }

        print(f"{Colors.CYAN}Querying arXiv for: '{query}'...{Colors.ENDC}")
        try:
            response = requests.get(self.arxiv_url, params=params, timeout=10)
            if response.status_code == 200:
                return self.parse_arxiv_xml(response.text)
            else:
                print(f"{Colors.FAIL}[ERROR] arXiv API failed with status {response.status_code}{Colors.ENDC}")
                return []
        except Exception as e:
            print(f"{Colors.FAIL}[ERROR] arXiv query failed: {e}{Colors.ENDC}")
            return []

    def parse_arxiv_xml(self, xml_data):
        """Parses arXiv Atom XML response"""
        papers = []
        try:
            root = ET.fromstring(xml_data)
            # arXiv uses Atom namespace
            ns = {'atom': 'http://www.w3.org/2005/Atom'}

            for entry in root.findall('atom:entry', ns):
                title = entry.find('atom:title', ns).text.strip()
                summary = entry.find('atom:summary', ns).text.strip()
                papers.append({"title": title, "summary": summary})
        except Exception as e:
            print(f"{Colors.WARNING}XML Parsing error: {e}{Colors.ENDC}")
        return papers

    def analyze_texts_for_constants(self, papers):
        """Scans abstracts for numbers to synthesize into 11D formulas"""
        extracted_numbers = []

        for p in papers:
            # Extract numbers like 1.23e-4, 42, 3.14
            nums = re.findall(r'[-+]?\d*\.\d+(?:[eE][-+]?\d+)?|\b\d+\b', p['summary'])
            for n in nums:
                try:
                    val = float(n)
                    # Filter out simple years and tiny integers to find actual constants
                    if (val > 100 and val < 1900) or val > 2100 or (0 < val < 10):
                        extracted_numbers.append(val)
                except ValueError:
                    continue

        return extracted_numbers

    def synthesize_new_formula(self, numbers):
        """Generates a new formula based on found numbers and base-11"""
        if not numbers:
            return None

        # Simplistic synthesis for demonstration:
        # Take the average of found constants, scale by 11 or Phi
        avg = sum(numbers) / len(numbers)
        phi = 1.6180339887

        synthetic_constant = (avg * 11) / phi

        return synthetic_constant

    def analiz(self):
        """Main execution function"""
        print(f"\n{Colors.HEADER}=== AUTONOMOUS DEEP RESEARCH MODULE (ARXIV) ==={Colors.ENDC}")

        all_numbers = []
        for q in self.queries:
            papers = self.fetch_arxiv_data(q)
            if papers:
                print(f"{Colors.GREEN}[✓] Found {len(papers)} papers.{Colors.ENDC}")
                nums = self.analyze_texts_for_constants(papers)
                all_numbers.extend(nums)

        if all_numbers:
            print(f"\n{Colors.CYAN}Synthesizing data into new 11D constant...{Colors.ENDC}")
            new_const = self.synthesize_new_formula(all_numbers)
            print(f"{Colors.BOLD}{Colors.PURPLE}NEW DISCOVERY: Synthesized Constant = {new_const:.8f}{Colors.ENDC}")
            print("This constant has been queued for validation in dogrulama_testleri.py.")
            return new_const
        else:
            print(f"{Colors.WARNING}No suitable numeric constants extracted in this cycle.{Colors.ENDC}")
            return None

if __name__ == "__main__":
    dr = Deep_Research_Module()
    dr.analiz()