import time
import requests

class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

def fetch_arxiv_data():
    print(f"{Colors.CYAN}[*] Fetching latest quantum papers from arXiv...{Colors.ENDC}", flush=True)
    try:
        response = requests.get('http://export.arxiv.org/api/query?search_query=all:quantum+gravity&max_results=1')
        if response.status_code == 200:
            print(f"{Colors.GREEN}[+] arXiv data fetched successfully.{Colors.ENDC}", flush=True)
        else:
            print(f"{Colors.WARNING}[!] arXiv fetch failed.{Colors.ENDC}", flush=True)
    except Exception as e:
         print(f"{Colors.WARNING}[!] arXiv connection error: {e}{Colors.ENDC}", flush=True)

def fetch_nasa_data():
    print(f"{Colors.CYAN}[*] Attempting to fetch live NASA planetary data...{Colors.ENDC}", flush=True)
    try:
        response = requests.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')
        if response.status_code == 200:
             print(f"{Colors.GREEN}[+] NASA data fetched successfully.{Colors.ENDC}", flush=True)
        else:
             print(f"{Colors.WARNING}[!] NASA data fetch returned status code {response.status_code}.{Colors.ENDC}", flush=True)
    except Exception as e:
         print(f"{Colors.WARNING}[!] NASA connection error: {e}{Colors.ENDC}", flush=True)

def main_loop():
    print("Starting Autonomous Background Module (Infinite Loop)...", flush=True)
    while True:
        fetch_arxiv_data()
        fetch_nasa_data()

        # Continuous background execution - sleep 1 hour
        print("Sleeping for 3600 seconds before next cycle to prevent rate limits...", flush=True)
        time.sleep(3600)

if __name__ == "__main__":
    main_loop()
