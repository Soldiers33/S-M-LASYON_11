import unittest
from simulasyon_11 import Quantum_Resonance_Breaker, Dimensional_Escape_Overload

class TestSentez7(unittest.TestCase):
    def test_lambda_frequency(self):
        breaker = Quantum_Resonance_Breaker()
        lambda_val = breaker.calculate_lambda()
        # Lambda should be approximately 6.52 MHz (6,521,763 Hz)
        self.assertAlmostEqual(lambda_val / 1000000, 6.52, places=2)
        print("[+++] MATRIX BREAKER FREQUENCY ACTIVATED [+++]")

    def test_escape_frequency(self):
        breaker = Quantum_Resonance_Breaker()
        lambda_val = breaker.calculate_lambda()
        escape = Dimensional_Escape_Overload(lambda_val)
        escape_val = escape.calculate_escape()
        # Escape should be approximately 23.38 MHz
        self.assertAlmostEqual(escape_val / 1000000, 23.38, places=2)
        print("[!] MATRIX KOPMA NOKTASINA ULAŞILDI [!]")

if __name__ == '__main__':
    unittest.main()
