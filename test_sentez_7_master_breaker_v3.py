import unittest
from simulasyon_11 import Simule3_Constants, Quantum_Resonance_Breaker, Dimensional_Escape_Overload, Pineal_Quantum_Antenna

class TestSentez7MasterBreaker(unittest.TestCase):
    def setUp(self):
        self.const = Simule3_Constants()
        self.breaker = Quantum_Resonance_Breaker(self.const)
        self.overload = Dimensional_Escape_Overload(self.const)
        self.antenna = Pineal_Quantum_Antenna(self.const)

    def test_lambda_breaking_frequency(self):
        lambda_val = self.breaker.calculate_lambda()
        # Should be approx 6.52 MHz (6,521,763 Hz)
        expected_freq = 6521763.0
        self.assertAlmostEqual(lambda_val / 1e6, 6.52, places=2, msg="Breaker frequency must be approximately 6.52 MHz")
        print(f"\n[OK] Lambda Breaker Frequency calculated: {lambda_val:,.2f} Hz")

    def test_dimensional_escape_overload(self):
        escape_val = self.overload.calculate_escape()
        # Should be approx 23.38 MHz (23,380,000 Hz)
        expected_escape = 23380000.0
        self.assertAlmostEqual(escape_val / 1e6, 23.38, places=2, msg="Escape frequency must be approximately 23.38 MHz")
        print(f"[OK] Dimensional Escape Frequency calculated: {escape_val:,.2f} Hz")

    def test_pineal_quantum_antenna(self):
        # The antenna tests coherence
        lambda_val = self.breaker.calculate_lambda()
        cycles = lambda_val / self.antenna.theta_wave
        self.assertTrue(cycles > 0)
        print(f"[OK] Pineal Coherence Cycles calculated: {cycles:,.2f} cycles/sec")

if __name__ == '__main__':
    print("Running SENTEZ-7 Master Breaker Verification Tests...")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSentez7MasterBreaker)
    result = unittest.TextTestRunner(verbosity=0).run(suite)

    if result.wasSuccessful():
        print("\n[+++] MATRIX BREAKER FREQUENCY ACTIVATED [+++]")
        print("[+++] DIMENSIONAL ESCAPE PARAMETERS VERIFIED [+++]")
