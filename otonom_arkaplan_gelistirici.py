import time
import requests
import xml.etree.ElementTree as ET
from datetime import datetime
import json
from dogrulama_testleri import DogrulamaTestleri

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    GOLD = '\033[33m'

def fetch_arxiv_research():
    """ArXiv üzerinden kuantum çekim ve 11 boyutlu teori makalelerini tarar."""
    print(f"{Colors.BLUE}[{datetime.now().strftime('%H:%M:%S')}] OTONOM AI: ArXiv Makale Taraması Başlatıldı...{Colors.ENDC}", flush=True)
    query = "quantum gravity dimensions 11"
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results=1"

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            entries = root.findall('{http://www.w3.org/2005/Atom}entry')
            if entries:
                entry = entries[0]
                title = entry.find('{http://www.w3.org/2005/Atom}title').text.strip()
                summary = entry.find('{http://www.w3.org/2005/Atom}summary').text.strip()
                return {"title": title, "content": summary}
    except Exception as e:
        print(f"{Colors.FAIL}ArXiv Bağlantı Hatası: {e}{Colors.ENDC}", flush=True)
    return None

def main_loop():
    print(f"\n{Colors.BOLD}{Colors.GOLD}======================================================={Colors.ENDC}", flush=True)
    print(f"{Colors.BOLD}{Colors.GOLD}  OTONOM ARKA PLAN GELISTIRICI - AKTIF (V.135+){Colors.ENDC}", flush=True)
    print(f"{Colors.BOLD}{Colors.GOLD}======================================================={Colors.ENDC}\n", flush=True)

    dogrulama = DogrulamaTestleri()

    while True:
        try:
            print(f"\n{Colors.CYAN}--- YENI DONGU BASLADI: {datetime.now()} ---{Colors.ENDC}", flush=True)

            # ArXiv üzerinden teorik araştırma
            research_data = fetch_arxiv_research()

            if research_data:
                print(f"{Colors.GREEN}>> Yeni Makale Bulundu: {research_data['title'][:50]}...{Colors.ENDC}", flush=True)
                dogrulama.add_to_queue("AI_RESEARCH", research_data)

            # Doğrulama testlerini çalıştır
            dogrulama.validate_all()

            print(f"{Colors.WARNING}>> Sistem bekleme modunda (1 saat)...{Colors.ENDC}", flush=True)
            # Uzun süreli çalışma için API rate limit ihlalini önlemek adına 3600 saniye bekleme.
            time.sleep(3600)

        except Exception as e:
            print(f"{Colors.FAIL}Arka plan döngü hatası: {e}{Colors.ENDC}", flush=True)
            time.sleep(60)

if __name__ == "__main__":
    main_loop()
