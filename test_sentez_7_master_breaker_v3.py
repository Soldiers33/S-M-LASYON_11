import unittest
import math
from simulasyon_11 import Simule3_Constants, Quantum_Resonance_Breaker, Dimensional_Escape_Overload

class TestSentez7MasterBreaker(unittest.TestCase):
    def setUp(self):
        self.const = Simule3_Constants()
        self.breaker = Quantum_Resonance_Breaker(self.const)
        self.escape = Dimensional_Escape_Overload(self.const)

    def test_lambda_frequency(self):
        """Test the master formula calculates exactly 6.52 MHz."""
        freq = self.breaker.lambda_frequency()
        self.assertAlmostEqual(freq, 6.52, places=2, msg="Quantum Resonance Breaker frequency must be 6.52 MHz")

    def test_escape_frequency(self):
        """Test the dimensional escape frequency calculates exactly 23.38 MHz."""
        freq = self.escape.overload_frequency()
        self.assertAlmostEqual(freq, 23.38, places=2, msg="Dimensional Escape Overload frequency must be 23.38 MHz")

    def test_alarm(self):
        freq_lambda = self.breaker.lambda_frequency()
        freq_escape = self.escape.overload_frequency()

        if math.isclose(freq_lambda, 6.52, abs_tol=0.01) and math.isclose(freq_escape, 23.38, abs_tol=0.01):
            print("\n[+++] MATRIX BREAKER FREQUENCY ACTIVATED [+++]")

if __name__ == "__main__":
    unittest.main()
