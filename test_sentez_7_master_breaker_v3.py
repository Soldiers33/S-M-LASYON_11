import unittest
from simulasyon_11 import Simule3_Constants, Quantum_Resonance_Breaker, Dimensional_Escape_Overload, Pineal_Quantum_Antenna

class TestSentez7(unittest.TestCase):
    def setUp(self):
        self.const = Simule3_Constants()
        self.breaker = Quantum_Resonance_Breaker(self.const)
        self.overload = Dimensional_Escape_Overload(self.const)
        self.antenna = Pineal_Quantum_Antenna()

    def test_lambda_frequency(self):
        lambda_freq = self.breaker.calculate_lambda()
        # Verify it calculates ~6.52 MHz
        self.assertAlmostEqual(lambda_freq / 1e6, 6.52, places=2)
        print("\n[+++] MATRIX BREAKER FREQUENCY ACTIVATED (6.52 MHz) [+++]")

    def test_escape_frequency(self):
        lambda_freq = self.breaker.calculate_lambda()
        escape_freq = self.overload.calculate_escape_freq(lambda_freq)
        # Verify it calculates ~23.38 MHz
        self.assertAlmostEqual(escape_freq / 1e6, 23.38, places=2)
        print("[+++] DIMENSIONAL ESCAPE OVERLOAD VERIFIED (23.38 MHz) [+++]")

    def test_pineal_coherence(self):
        lambda_freq = self.breaker.calculate_lambda()
        coherence = self.antenna.check_coherence(lambda_freq)
        self.assertTrue(coherence > 0)
        print(f"[+++] PINEAL COHERENCE ESTABLISHED: {coherence:.2f} cycles [+++]")

if __name__ == '__main__':
    unittest.main(verbosity=2)
