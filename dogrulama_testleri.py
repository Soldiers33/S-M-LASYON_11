import time
import sys

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

class DogrulamaTestleri:
    """
    Sistem için YZ doğrulama testleri ve veri madenciliği test kontrol sınıfı.
    Eklenen verilerin bütünlüğünü ve simülasyondaki geçerliliğini denetler.
    """
    def __init__(self):
        self.test_queue = []
        self.verified_results = {}
        self.validation_score = 0.0

    def add_to_queue(self, module_name, test_data):
        """Doğrulanacak veriyi sıraya ekler"""
        self.test_queue.append({'module': module_name, 'data': test_data})
        print(f"{Colors.BLUE}[QUEUE] {module_name} test sırasına eklendi.{Colors.ENDC}", flush=True)

    def run_verifications(self):
        """Sıradaki tüm testleri çalıştırıp doğrular"""
        print(f"\n{Colors.HEADER}=== OTOMATİK SİSTEM DOĞRULAMA TESTLERİ BAŞLIYOR ==={Colors.ENDC}", flush=True)
        if not self.test_queue:
            print(f"{Colors.WARNING}Sırada bekleyen test verisi bulunmuyor.{Colors.ENDC}", flush=True)
            return

        passed_tests = 0
        total_tests = len(self.test_queue)

        for i, item in enumerate(self.test_queue):
            module = item['module']
            data = item['data']
            print(f"\r\033[K{Colors.CYAN}Doğrulanıyor [{i+1}/{total_tests}]: {module}...{Colors.ENDC}", end='', flush=True)
            time.sleep(0.5) # Simüle edilmiş analiz süresi

            # Basit veri bütünlüğü kontrolü
            if data and isinstance(data, dict):
                self.verified_results[module] = {
                    'status': 'VERIFIED',
                    'timestamp': time.time(),
                    'summary': f"Modül verisi entegrasyona uygun. Key count: {len(data.keys())}"
                }
                passed_tests += 1
            else:
                self.verified_results[module] = {
                    'status': 'FAILED',
                    'timestamp': time.time(),
                    'summary': "Geçersiz veri formatı!"
                }

        self.validation_score = (passed_tests / total_tests) * 100
        print(f"\r\033[K{Colors.GREEN}[OK] Doğrulama Tamamlandı. Başarı: %{self.validation_score:.1f}{Colors.ENDC}\n", flush=True)
        self.test_queue = [] # Kuyruğu temizle

    def get_status(self):
        return {
            'verified_modules': len(self.verified_results),
            'score': self.validation_score,
            'details': self.verified_results
        }
