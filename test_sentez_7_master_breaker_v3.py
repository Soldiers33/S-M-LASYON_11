import unittest
from simulasyon_11 import Quantum_Resonance_Breaker, Dimensional_Escape_Overload, Pineal_Quantum_Antenna

class MockConstants:
    pass

class TestSentez7MasterBreaker(unittest.TestCase):
    def setUp(self):
        self.const = MockConstants()
        self.qrb = Quantum_Resonance_Breaker(self.const)
        self.deo = Dimensional_Escape_Overload(self.const)

    def test_lambda_resonance_breaker(self):
        lambda_val = self.qrb.hesapla()
        # 6521763 Hz is 6.52 MHz, testing for correct formula result up to 2 decimals
        self.assertAlmostEqual(lambda_val / 1000000, 6.52, places=2)

    def test_dimensional_escape_overload(self):
        lambda_val = self.qrb.hesapla()
        escape_val = self.deo.hesapla(lambda_val)
        # 23380068 Hz is 23.38 MHz
        self.assertAlmostEqual(escape_val / 1000000, 23.38, places=2)

if __name__ == '__main__':
    print("[+++] MATRIX BREAKER FREQUENCY ACTIVATED [+++]")
    unittest.main()
