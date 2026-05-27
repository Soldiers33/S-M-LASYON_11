import math
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
    Active Validation Queue to test new findings.
    Validates data against the 11-dimensional framework and R11 constants.
    """
    def __init__(self):
        self.validation_queue = []
        self.R11 = 11111111111
        self.BASE_SYSTEM = 11

    def add_to_queue(self, source, data_type, value, description):
        """Add a new finding to the validation queue."""
        self.validation_queue.append({
            "source": source,
            "data_type": data_type,
            "value": value,
            "description": description,
            "timestamp": datetime.datetime.now().isoformat()
        })
        print(f"{Colors.BLUE}[QUEUE] Added {data_type} from {source}: {value}{Colors.ENDC}")

    def run_all_validations(self):
        """Run validation checks on all items in the queue."""
        print(f"\n{Colors.HEADER}=== RUNNING VALIDATION QUEUE ==={Colors.ENDC}")
        if not self.validation_queue:
            print(f"{Colors.WARNING}Validation queue is empty.{Colors.ENDC}")
            return

        for item in self.validation_queue:
            print(f"{Colors.CYAN}Validating {item['source']} - {item['data_type']}{Colors.ENDC}")
            val = item['value']

            # Simple float or int validation
            if isinstance(val, (int, float)):
                # Check for resonance with 11
                if val != 0 and (val % self.BASE_SYSTEM == 0 or math.isclose(val % self.BASE_SYSTEM, 0, abs_tol=0.01) or
                                 math.isclose(self.R11 % val, 0, abs_tol=0.1)):
                    print(f"  {Colors.GREEN}[VERIFIED] Value {val} resonates with 11-dimensional baseline.{Colors.ENDC}")
                else:
                    print(f"  {Colors.WARNING}[PENDING] Value {val} requires deeper dimensional alignment check.{Colors.ENDC}")
            elif isinstance(val, dict):
                print(f"  {Colors.BLUE}[ANALYSIS] Analyzing complex data structure...{Colors.ENDC}")
                # check dict values
                for k, v in val.items():
                     if isinstance(v, (int, float)):
                         if v != 0 and (v % self.BASE_SYSTEM == 0 or math.isclose(v % self.BASE_SYSTEM, 0, abs_tol=0.01)):
                             print(f"    {Colors.GREEN}[VERIFIED] Sub-parameter {k}={v} resonates with 11.{Colors.ENDC}")
            else:
                 print(f"  {Colors.BLUE}[INFO] Value type {type(val)} logged for historical analysis.{Colors.ENDC}")

        print(f"{Colors.GREEN}=== VALIDATION QUEUE COMPLETED ==={Colors.ENDC}\n")
        self.validation_queue.clear()
