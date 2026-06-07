import time
import sys
from dogrulama_testleri import DogrulamaTestleri
from modul_nasa_live_data import ModulNasaLiveData
from deep_research_module import DeepResearchModule

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def arkaplan_dongusu():
    print(f"{Colors.HEADER}{Colors.BOLD}=== OTONOM ARKA PLAN GELİŞTİRİCİ BAŞLATILDI ==={Colors.ENDC}", flush=True)

    dogrulama = DogrulamaTestleri()
    nasa = ModulNasaLiveData()
    research = DeepResearchModule()

    dongu_sayisi = 0
    try:
        while True:
            dongu_sayisi += 1
            print(f"\n{Colors.BLUE}--- Arka Plan Döngüsü: {dongu_sayisi} ---{Colors.ENDC}", flush=True)

            # 1. Fetch NASA Data
            nasa_veri = nasa.fetch_latest_data()
            dogrulama.add_to_queue(
                data_point=nasa_veri.get('extracted_constants'),
                source=nasa_veri.get('source', 'NASA'),
                description="Live Astrophysical Constants"
            )

            # 2. Deep Research on arXiv
            makaleler = research.search_arxiv(query="dark energy 11 dimensions", max_results=2)
            if makaleler:
                yeni_formul = research.synthesize_new_formula(makaleler)
                dogrulama.add_to_queue(
                    data_point=yeni_formul,
                    source="arXiv Deep Research",
                    description=yeni_formul.get('formula_name', 'Unknown Formula')
                )

            # 3. Run Validation
            dogrulama.run_verification()

            # Prevent API rate limiting and excessive CPU usage
            print(f"{Colors.CYAN}Arka plan işlemleri tamamlandı. Bekleniyor...{Colors.ENDC}", flush=True)
            # Long sleep to avoid hitting API limits continuously
            time.sleep(3600)

    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}Arka plan geliştirici durduruldu.{Colors.ENDC}", flush=True)
        sys.exit(0)

if __name__ == "__main__":
    arkaplan_dongusu()
