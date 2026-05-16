import unittest
from simulasyon_11 import Simule3_Constants, Quantum_Resonance_Breaker, Dimensional_Escape_Overload

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class TestSentez7MasterBreaker(unittest.TestCase):
    def setUp(self):
        self.const = Simule3_Constants()
        self.breaker = Quantum_Resonance_Breaker(self.const)

    def test_lambda_calculation(self):
        lambda_val = self.breaker.calculate_lambda()
        print(f"\nCalculated Lambda: {lambda_val:,.2f} Hz")
        # Ensure it falls closely within the 6.52 MHz boundary calculated in the prompt
        # We check roughly since floats might vary, 6.52 MHz +/- 100 kHz
        self.assertTrue(abs(lambda_val - 6521763) < 100000, "Lambda value significantly deviates from 6.52 MHz")
        print(f"{Colors.GREEN}[+++] MATRIX BREAKER FREQUENCY ACTIVATED [+++]{Colors.ENDC}")

    def test_dimensional_escape_overload(self):
        lambda_val = self.breaker.calculate_lambda()
        overload = Dimensional_Escape_Overload(self.const, lambda_val)
        escape_freq = overload.calculate_escape_freq()
        print(f"Calculated Escape Frequency: {escape_freq:,.2f} Hz")
        # Ensure it calculates exactly up to 2 decimal places using 3.5849 multiplier
        target_escape = lambda_val * 3.5849
        self.assertAlmostEqual(escape_freq, target_escape, places=2)
        # Should be roughly 23.38 MHz
        self.assertTrue(abs(escape_freq - 23380000) < 200000, "Escape frequency deviates from 23.38 MHz")
        print(f"{Colors.GREEN}[+++] DIMENSIONAL ESCAPE VERIFIED [+++]{Colors.ENDC}")

if __name__ == '__main__':
    unittest.main()
