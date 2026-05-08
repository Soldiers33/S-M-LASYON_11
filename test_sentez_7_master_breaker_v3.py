import unittest
from simulasyon_11 import Quantum_Resonance_Breaker, Dimensional_Escape_Overload

class TestSentez7MasterBreaker(unittest.TestCase):
    def setUp(self):
        self.breaker = Quantum_Resonance_Breaker()
        self.lambda_freq = self.breaker.calculate_lambda()
        self.overload = Dimensional_Escape_Overload(self.lambda_freq)

    def test_lambda_breaker_frequency(self):
        # 6.52 MHz Anti-Gravity baseline frequency
        expected_freq = 6.52
        self.assertAlmostEqual(self.lambda_freq, expected_freq, places=2)

    def test_dimensional_escape_frequency(self):
        # 23.38 MHz Overload / Disconnect frequency
        expected_escape = 23.38
        escape_freq = self.overload.calculate_escape_freq()
        self.assertAlmostEqual(escape_freq, expected_escape, places=2)

if __name__ == "__main__":
    unittest.main()
