import unittest
import math
from simulasyon_11 import Quantum_Resonance_Breaker, Dimensional_Escape_Overload, Pineal_Quantum_Antenna

class TestSentez7MasterBreaker(unittest.TestCase):

    def setUp(self):
        self.breaker = Quantum_Resonance_Breaker()
        self.escape = Dimensional_Escape_Overload()
        self.pineal = Pineal_Quantum_Antenna()

    def test_lambda_calculation(self):
        # Master formula check
        freq = self.breaker.calculate_lambda()
        # Expect ~6.52 MHz (6521763 Hz)
        self.assertAlmostEqual(freq / 1e6, 6.52, places=2)
        print(f"\n[OK] Lambda Break Frequency: {freq / 1e6:.2f} MHz")

    def test_dimensional_escape(self):
        # 23.38 MHz escape velocity check
        freq = self.escape.calculate_escape_freq()
        self.assertAlmostEqual(freq / 1e6, 23.38, places=2)
        print(f"[OK] Dimensional Escape Frequency: {freq / 1e6:.2f} MHz")

    def test_pineal_antenna(self):
        self.assertEqual(self.pineal.theta_wave, 8.0)
        self.assertEqual(self.pineal.target_mhz, 6.52)
        print("[OK] Pineal Antenna Config Validated")

if __name__ == "__main__":
    print("\n[+++] RUNNING SENTEZ-7 TESTS [+++]")
    unittest.main(exit=False)
    print("[+++] MATRIX BREAKER FREQUENCY ACTIVATED [+++]\n")
