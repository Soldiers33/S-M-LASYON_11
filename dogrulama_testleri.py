import datetime

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    GOLD = '\033[33m'
    MAGENTA = '\033[35m'
    PURPLE = '\033[35m'

class DogrulamaTestleri:
    """
    Simülasyona eklenen her yeni verinin 11 tabanlı Evrensel Matrise uygunluğunu
    ve kimlik/ID doğrulamalarını yapan Güvenlik Modülü.
    """
    def __init__(self):
        self.validation_queue = []
        self.r11 = 11111111111
        self.ideal_moon_perigee = 363000

    def add_to_queue(self, source, data):
        """Doğrulama kuyruğuna yeni veri ekler."""
        self.validation_queue.append({
            'source': source,
            'data': data,
            'timestamp': datetime.datetime.now()
        })
        print(f"{Colors.BLUE}[QUEUE] {source} kaynağından veri kuyruğa eklendi. ({len(self.validation_queue)} bekleyen){Colors.ENDC}")

    def validate_nasa_data(self, data):
        """NASA'dan gelen verilerin matematiksel tutarlılığını test eder."""
        print(f"{Colors.CYAN}  -> NASA Verisi Doğrulanıyor...{Colors.ENDC}")
        nasa_live = data.get('nasa_live', {})
        formuller = data.get('yeni_formuller', {})

        # Test 1: API Status
        if nasa_live.get('moon_api_status') != 'SUCCESS':
            print(f"{Colors.FAIL}    ❌ NASA API durumu BAŞARISIZ. Doğrulama red.{Colors.ENDC}")
            return False

        # Test 2: R11 Çarpan Bağı
        r11_bag = formuller.get('r11_kozmik_bag', {}).get('bag_katsayisi', 0)
        if r11_bag <= 0:
            print(f"{Colors.FAIL}    ❌ R11 Kapsamı ihlali. Doğrulama red.{Colors.ENDC}")
            return False

        # Test 3: Kuantum Dalgalanma Sınırı
        kuantum_kati = formuller.get('kuantum_cekim_dalga', {}).get('kuantum_kati', 0)
        if not (0.9 < kuantum_kati < 1.2): # %20 sapmaya izin ver
            print(f"{Colors.FAIL}    ❌ Kuantum Dalgalanması sınırlar dışında: {kuantum_kati}. Doğrulama red.{Colors.ENDC}")
            return False

        print(f"{Colors.GREEN}    ✅ NASA Verisi Simüle3 Matrisine UYGUN.{Colors.ENDC}")
        return True

    def validate_ai_research(self, data):
        """Otonom AI tarafından arxiv/derin arama ile getirilen verileri test eder."""
        print(f"{Colors.CYAN}  -> AI Araştırma Verisi Doğrulanıyor...{Colors.ENDC}")
        content = data.get('content', '').lower()
        if not content:
            print(f"{Colors.FAIL}    ❌ İçerik boş. Doğrulama red.{Colors.ENDC}")
            return False

        # Anahtar Kelime Doğrulaması (ID Doğrulaması)
        keywords = ['quantum', 'gravity', '11', 'dimension', 'space', 'time', 'physics', 'astrophysics']
        found = sum(1 for kw in keywords if kw in content)

        if found < 1:
            print(f"{Colors.WARNING}    ⚠️ AI Araştırmasında 11-Boyutlu Sistem Anahtarları Yetersiz. Red.{Colors.ENDC}")
            return False

        print(f"{Colors.GREEN}    ✅ AI Araştırması 11-Boyutlu Sisteme UYGUN. (Kesişen Anahtarlar: {found}){Colors.ENDC}")
        return True

    def validate_all(self):
        """Kuyruktaki tüm verileri test eder ve onaylıları sisteme entegre kabul eder."""
        print(f"\n{Colors.BOLD}{Colors.GOLD}===================================================={Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.GOLD}  [DOGRULAMA] 11-BOYUTLU MATRİS İÇERİK KONTROLÜ{Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.GOLD}===================================================={Colors.ENDC}")

        if not self.validation_queue:
            print(f"{Colors.WARNING}Kuyrukta doğrulanacak veri yok.{Colors.ENDC}")
            return

        passed_count = 0
        total_count = len(self.validation_queue)

        for item in self.validation_queue:
            source = item['source']
            print(f"\n{Colors.PURPLE}Test Ediliyor: {source}{Colors.ENDC} (Zaman: {item['timestamp']})")

            is_valid = False
            if source == 'NASA_LIVE':
                is_valid = self.validate_nasa_data(item['data'])
            elif source == 'AI_RESEARCH':
                is_valid = self.validate_ai_research(item['data'])
            else:
                print(f"{Colors.WARNING}    ⚠️ Bilinmeyen kaynak: {source}. Standart kabul uygulandı.{Colors.ENDC}")
                is_valid = True

            if is_valid:
                passed_count += 1

        self.validation_queue.clear()

        print(f"\n{Colors.BOLD}{Colors.CYAN}DOGRULAMA SONUCU: {passed_count}/{total_count} BAŞARILI.{Colors.ENDC}\n")
        return passed_count == total_count

if __name__ == "__main__":
    # Test execution
    dogrulama = DogrulamaTestleri()
    # Mock data
    nasa_mock = {
        'nasa_live': {'moon_api_status': 'SUCCESS'},
        'yeni_formuller': {
            'r11_kozmik_bag': {'bag_katsayisi': 28000},
            'kuantum_cekim_dalga': {'kuantum_kati': 1.05}
        }
    }
    ai_mock = {'content': 'Quantum gravity in 11 dimensions is a widely researched topic in physics.'}
    bad_ai_mock = {'content': 'Just a normal text about baking a cake.'}

    dogrulama.add_to_queue('NASA_LIVE', nasa_mock)
    dogrulama.add_to_queue('AI_RESEARCH', ai_mock)
    dogrulama.add_to_queue('AI_RESEARCH', bad_ai_mock)

    dogrulama.validate_all()
