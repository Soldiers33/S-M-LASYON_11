import math

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

class Yeni_Dogrulama:
    """
    Validation tests for AI-discovered data against 11-Dimensional Rules.
    Acts as an active data integrity monitor.
    """
    def __init__(self):
        self.validation_queue = []

    def add_to_queue(self, value, source):
        self.validation_queue.append({"value": value, "source": source})

    def check_11_divisibility(self, value):
        """Checks if a float is closely related to a multiple of 11."""
        # Simple heuristic: is it within 1% of a multiple of 11?
        nearest_multiple = round(value / 11) * 11
        if nearest_multiple == 0:
            return False
        deviation = abs(value - nearest_multiple) / nearest_multiple
        return deviation < 0.01

    def check_phi_resonance(self, value):
        phi = 1.6180339887
        val_mod_phi = value % phi
        # If it closely resonates with phi
        return val_mod_phi < 0.05 or (phi - val_mod_phi) < 0.05

    def analiz(self):
        print(f"\n{Colors.HEADER}=== ACTIVE DATA INTEGRITY MONITOR (VALIDATION) ==={Colors.ENDC}")
        if not self.validation_queue:
            print(f"{Colors.GREEN}[OK] No new discoveries in queue to validate.{Colors.ENDC}")

        for item in self.validation_queue:
            val = item["value"]
            src = item["source"]
            print(f"{Colors.CYAN}Validating Discovery from {src}: {val:.4f}{Colors.ENDC}")

            is_11 = self.check_11_divisibility(val)
            is_phi = self.check_phi_resonance(val)

            if is_11:
                print(f"{Colors.GREEN}  [✓] 11-Divisibility Resonance Verified.{Colors.ENDC}")
            else:
                print(f"{Colors.WARNING}  [!] 11-Divisibility Weak/Missing.{Colors.ENDC}")

            if is_phi:
                print(f"{Colors.GREEN}  [✓] Golden Ratio (Phi) Resonance Verified.{Colors.ENDC}")
            else:
                print(f"{Colors.WARNING}  [!] Phi Resonance Weak/Missing.{Colors.ENDC}")

            if is_11 or is_phi:
                print(f"{Colors.BOLD}{Colors.GREEN}>> INTEGRITY CHECK PASSED: Authorized for Levh-i Mahfuz DB.<<{Colors.ENDC}")
            else:
                print(f"{Colors.FAIL}>> INTEGRITY CHECK FAILED: Rejected by base matrix.<<{Colors.ENDC}")

if __name__ == "__main__":
    vd = Yeni_Dogrulama()
    vd.analiz()