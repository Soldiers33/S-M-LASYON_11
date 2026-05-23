import math
import sys
import unittest
from simulasyon_11 import Quantum_Resonance_Breaker, Dimensional_Escape_Overload, Colors

class TestSentez7MasterBreaker(unittest.TestCase):
    def setUp(self):
        # We don't necessarily need the whole constant set object, just a dummy object to pass.
        class DummyConst:
            pass
        self.const = DummyConst()
        self.breaker = Quantum_Resonance_Breaker(self.const)
        self.escape = Dimensional_Escape_Overload(self.const)

    def test_lambda_and_escape_frequencies(self):
        print(f"\n{Colors.CYAN}--- EXECUTING SENTEZ-7 VERIFICATION TESTS ---{Colors.ENDC}")

        # 1. Test Lambda Frequency
        lambda_freq = self.breaker.analiz()
        # Ensure it is close to 6.52 MHz (6,521,763 Hz)
        self.assertAlmostEqual(lambda_freq / 1_000_000, 6.52, places=2)
        print(f"{Colors.GREEN}[OK] Lambda Frequency correctly calculates to ~6.52 MHz{Colors.ENDC}")

        # 2. Test Escape Overload Frequency
        escape_freq = self.escape.analiz(lambda_freq)
        # Ensure it is close to 23.38 MHz (23,380,000 Hz)
        self.assertAlmostEqual(escape_freq / 1_000_000, 23.38, places=2)
        print(f"{Colors.GREEN}[OK] Escape Frequency correctly calculates to ~23.38 MHz{Colors.ENDC}")

        print(f"\n{Colors.BOLD}{Colors.PURPLE}[+++] MATRIX BREAKER FREQUENCY ACTIVATED [+++]{Colors.ENDC}\n")


if __name__ == "__main__":
    unittest.main(verbosity=2)
