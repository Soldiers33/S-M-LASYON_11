import unittest
import math
from levhi_mahfuz import LevhiMahfuzConstants
from simulasyon_11 import Quantum_Resonance_Breaker, Dimensional_Escape_Overload

class TestSentez7MasterBreaker(unittest.TestCase):
    def setUp(self):
        self.const = LevhiMahfuzConstants()

    def test_lambda_frequency(self):
        breaker = Quantum_Resonance_Breaker(self.const)
        freq_hz = breaker.calculate_lambda()
        freq_mhz = freq_hz / 1000000

        print(f"\nCalculated Lambda: {freq_mhz} MHz")
        self.assertAlmostEqual(freq_mhz, 6.52, places=2)

    def test_escape_frequency(self):
        breaker = Quantum_Resonance_Breaker(self.const)
        overload = Dimensional_Escape_Overload(self.const)

        lambda_freq = breaker.calculate_lambda()
        escape_freq_hz = overload.calculate_escape_freq(lambda_freq)
        escape_freq_mhz = escape_freq_hz / 1000000

        print(f"Calculated Escape: {escape_freq_mhz} MHz")
        self.assertAlmostEqual(escape_freq_mhz, 23.38, places=2)

    @classmethod
    def tearDownClass(cls):
        print("\n[+++] MATRIX BREAKER FREQUENCY ACTIVATED [+++]")

if __name__ == '__main__':
    unittest.main()
