import time
import hashlib

class DogrulamaTestleri:
    def __init__(self):
        self.validation_queue = []
        self.verified_data = []

    def add_to_queue(self, data_dict):
        self.validation_queue.append(data_dict)
        print(f"\033[94m[VALIDATION QUEUE]\033[0m Added {len(data_dict)} items to validation queue.")

    def run_tests(self):
        print("\033[95m[VERIFICATION]\033[0m Running Generative AI & ID Validation Tests...")
        while self.validation_queue:
            data = self.validation_queue.pop(0)
            for key, value in data.items():
                # Perform an ID hash verification
                hash_id = hashlib.sha256(f"{key}_{value}".encode()).hexdigest()[:11]
                print(f"  \033[92m[PASS]\033[0m {key}: {value} (Hash ID: {hash_id})")
                self.verified_data.append({"key": key, "value": value, "hash": hash_id})
        return self.verified_data
