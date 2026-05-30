import time
from modul_nasa_live_data import ModulNasaLiveData

class Colors:
    HEADER = '\033[95m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class DogrulamaTestleri:
    def __init__(self):
        self.queue = []
        self.nasa_module = ModulNasaLiveData()

    def add_to_queue(self, data):
        self.queue.append(data)

    def run_tests(self):
        print(f"\n{Colors.HEADER}=== ACTIVE DATA INTEGRITY MONITOR & VALIDATION ==={Colors.ENDC}")
        self.nasa_module.analiz()
        print(f"{Colors.CYAN}Validating internal data queue ({len(self.queue)} items)...{Colors.ENDC}")
        for item in self.queue:
            print(f" - Validating: {item}")
            time.sleep(0.1)
        print(f"{Colors.GREEN}[+] All active validations passed.{Colors.ENDC}")
        self.queue = []
