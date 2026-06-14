import time
import subprocess
import os

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def run_tests_and_validate():
    """Çeşitli doğrulama testlerini arkaplanda çalıştırır."""
    test_files = [
        "test_11_dimensional_constants.py",
        "test_dark_energy_matter_constants.py",
        "test_grok_verification.py",
        "test_population_discrepancy.py"
    ]

    print(f"\n{Colors.HEADER}=== OTONOM SİSTEM: TEST VE DOĞRULAMA RUTİNİ BAŞLATILIYOR ==={Colors.ENDC}", flush=True)

    for test_file in test_files:
        if os.path.exists(test_file):
            print(f"{Colors.CYAN}[OTONOM] Çalıştırılıyor: {test_file}...{Colors.ENDC}", flush=True)
            try:
                # Arkaplan süreç loglarında tutarlılık için stdout ve stderr'i loglayabiliriz
                result = subprocess.run(["python3", test_file], check=True, capture_output=True, text=True)
                print(f"{Colors.GREEN}[OTONOM] {test_file} BAŞARILI.{Colors.ENDC}", flush=True)
            except subprocess.CalledProcessError as e:
                print(f"{Colors.FAIL}[OTONOM] {test_file} BAŞARISIZ. Çıkış Kodu: {e.returncode}{Colors.ENDC}", flush=True)
        else:
            print(f"{Colors.WARNING}[OTONOM] {test_file} bulunamadı, atlanıyor.{Colors.ENDC}", flush=True)

def arkaplan_dongusu():
    """Arkaplanda sürekli veri çeken, test eden ve simülasyonu geliştiren ana döngü."""
    from modul_nasa_live_data import ModulNasaLiveData
    from deep_research_module import DeepResearchModule
    from dogrulama_testleri import DogrulamaTestleri

    nasa_module = ModulNasaLiveData()
    research_module = DeepResearchModule()
    dogrulama = DogrulamaTestleri()

    dongu_sayaci = 1

    print(f"{Colors.HEADER}--- OTONOM ARKA PLAN GELİŞTİRİCİ AKTİF ---{Colors.ENDC}", flush=True)

    while True:
        print(f"\n{Colors.BLUE}>>> DÖNGÜ {dongu_sayaci} BAŞLIYOR <<<{Colors.ENDC}", flush=True)

        # 1. Canlı verileri çek
        nasa_data = nasa_module.fetch_live_telemetry()
        dogrulama.add_to_queue("NASA_LIVE_TELEMETRY", nasa_data)

        # 2. Makaleleri tara (ArXiv)
        arxiv_data = research_module.fetch_quantum_papers()
        dogrulama.add_to_queue("ARXIV_QUANTUM_RESEARCH", arxiv_data)

        # 3. Elde edilen verileri doğrulama kuyruğundan geçir
        dogrulama.run_verifications()

        # 4. Sistem içi test komut dosyalarını otonom çalıştır
        run_tests_and_validate()

        print(f"{Colors.GREEN}<<< DÖNGÜ {dongu_sayaci} TAMAMLANDI. UYKU MODUNA GEÇİLİYOR. >>>{Colors.ENDC}", flush=True)

        # Gerçek bir sistemde bu 3600 saniye (1 saat) veya daha uzun olabilir.
        # Test ortamı olduğu için API limitlerine takılmamak adına uzun bir süre bekle.
        # Rate limit yememek için uyku.
        time.sleep(3600)
        dongu_sayaci += 1

if __name__ == "__main__":
    # Eğer doğrudan çalıştırılırsa, daemon olarak başlatılabilir
    try:
        arkaplan_dongusu()
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}Otonom arkaplan geliştirici durduruldu.{Colors.ENDC}")
