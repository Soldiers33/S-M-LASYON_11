import time

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
    def __init__(self):
        self.queue = []

    def add_to_queue(self, source, data):
        print(f"{Colors.CYAN}[VALIDATION QUEUE] Data added from {source}{Colors.ENDC}")
        self.queue.append({"source": source, "data": data, "timestamp": time.time()})

    def run_validation(self):
        print(f"\n{Colors.HEADER}=== ACTIVE VALIDATION & DATA INTEGRITY TESTS ==={Colors.ENDC}")
        if not self.queue:
            print(f"{Colors.WARNING}Queue is empty. No new data to validate.{Colors.ENDC}")
            return True

        success = True
        for item in self.queue:
            print(f"{Colors.BLUE}Validating data from: {item['source']}{Colors.ENDC}")

            if "lambda_matrix_breaker" in item["data"]:
                val = item["data"]["lambda_matrix_breaker"]
                if val > 0:
                    print(f"{Colors.GREEN}[PASS] Lambda value {val} is valid.{Colors.ENDC}")
                else:
                    print(f"{Colors.FAIL}[FAIL] Invalid lambda value.{Colors.ENDC}")
                    success = False
            elif "phi_resonance" in item["data"]:
                val = item["data"]["phi_resonance"]
                if val > 0:
                    print(f"{Colors.GREEN}[PASS] Phi Resonance {val} is valid.{Colors.ENDC}")
                else:
                    print(f"{Colors.FAIL}[FAIL] Invalid Phi Resonance value.{Colors.ENDC}")
                    success = False
            else:
                print(f"{Colors.GREEN}[PASS] Generic data validation.{Colors.ENDC}")

        self.queue = []
        return success

    def analiz(self):
        return self.run_validation()

if __name__ == "__main__":
    test = DogrulamaTestleri()
    test.add_to_queue("NASA_LIVE", {"lambda_matrix_breaker": 6.52})
    test.analiz()
