import unittest
import math
from simulasyon_11 import Quantum_Resonance_Breaker, Dimensional_Escape_Overload, Simule3_Constants

class TestSentez7MasterBreaker(unittest.TestCase):
    def setUp(self):
        self.const = Simule3_Constants()
        self.breaker = Quantum_Resonance_Breaker(self.const)

    def test_lambda_breaker_frequency(self):
        lambda_hz = self.breaker.calculate_lambda()
        lambda_mhz = lambda_hz / 1000000

        print(f"\nCalculated Lambda: {lambda_mhz:.2f} MHz")
        self.assertAlmostEqual(lambda_mhz, 6.52, places=2)
        print("[+++] MATRIX BREAKER FREQUENCY ACTIVATED [+++]")

    def test_escape_overload_frequency(self):
        lambda_hz = self.breaker.calculate_lambda()
        escape = Dimensional_Escape_Overload(lambda_hz)
        escape_hz = escape.calculate_escape()
        escape_mhz = escape_hz / 1000000

        print(f"\nCalculated Escape: {escape_mhz:.2f} MHz")
        self.assertAlmostEqual(escape_mhz, 23.38, places=2)
        print("[+++] DIMENSIONAL ESCAPE OVERLOAD VERIFIED [+++]")

if __name__ == '__main__':
    unittest.main()
