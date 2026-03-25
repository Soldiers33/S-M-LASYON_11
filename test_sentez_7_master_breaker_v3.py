import unittest
import math
import sys
from simulasyon_11 import Quantum_Resonance_Breaker, Dimensional_Escape_Overload, Pineal_Quantum_Antenna, Simule3_Constants

class TestSentez7MasterBreakerV3(unittest.TestCase):
    def setUp(self):
        self.const = Simule3_Constants()
        self.qrb = Quantum_Resonance_Breaker(self.const)
        self.deo = Dimensional_Escape_Overload(self.const)
        self.pqa = Pineal_Quantum_Antenna(self.const)

    def test_quantum_resonance_breaker(self):
        freq = self.qrb.analiz()
        self.assertAlmostEqual(freq, 6521763.484, places=2)
        print("\n[+++] MATRIX BREAKER FREQUENCY ACTIVATED [+++]")

    def test_dimensional_escape_overload(self):
        escape_freq = self.deo.analiz()
        self.assertEqual(escape_freq, 23386439.0)

    def test_pineal_quantum_antenna(self):
        theta, wifi = self.pqa.analiz()
        self.assertEqual(theta, 8.0)
        self.assertEqual(wifi, 6.52)

if __name__ == '__main__':
    unittest.main()
