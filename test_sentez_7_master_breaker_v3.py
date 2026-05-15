import math
import unittest
from simulasyon_11 import Quantum_Resonance_Breaker, Dimensional_Escape_Overload, Simule3_Constants, Pineal_Quantum_Antenna

class TestSentez7MasterBreaker(unittest.TestCase):
    def setUp(self):
        self.const = Simule3_Constants()
        self.breaker = Quantum_Resonance_Breaker(self.const)
        self.escape = Dimensional_Escape_Overload(self.const)
        self.antenna = Pineal_Quantum_Antenna(self.const)

    def test_lambda_calculation(self):
        # The target Lambda frequency is around 6.52 MHz (6,521,763 Hz)
        lambda_hz = self.breaker.calculate_lambda()
        target_hz = 6521763.0

        # Test if it's within an acceptable margin of error (e.g. 50 Hz difference due to precision)
        self.assertTrue(abs(lambda_hz - target_hz) < 50, f"Lambda Hz {lambda_hz} is not close enough to {target_hz}")

    def test_escape_frequency(self):
        # 6.52 MHz * 3.5849 = 23.38 MHz (23,380,000 Hz roughly)
        lambda_hz = self.breaker.calculate_lambda()
        escape_hz = self.escape.calculate_escape_freq(lambda_hz)
        target_escape_hz = 23380000.0

        self.assertTrue(abs(escape_hz - target_escape_hz) < 50000, f"Escape Hz {escape_hz} is not close enough to {target_escape_hz}")

if __name__ == "__main__":
    # Also run the modules' `analiz` to trigger the alarm print
    print("\n--- Running Module Analysis Outputs ---")
    const = Simule3_Constants()
    Quantum_Resonance_Breaker(const).analiz()
    Dimensional_Escape_Overload(const).analiz()
    Pineal_Quantum_Antenna(const).analiz()

    print("\n[+++] MATRIX BREAKER FREQUENCY ACTIVATED [+++]\n")

    print("--- Running Unit Tests ---")
    unittest.main()
