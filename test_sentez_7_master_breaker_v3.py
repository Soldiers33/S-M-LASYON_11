import unittest
from simulasyon_11 import Quantum_Resonance_Breaker, Dimensional_Escape_Overload, Colors

class TestSentez7MasterBreaker(unittest.TestCase):
    def test_lambda_frequency(self):
        breaker = Quantum_Resonance_Breaker()
        lambda_val = breaker.calculate_lambda()
        freq_mhz = lambda_val / 1000000
        print(f"Calculated Lambda (MHz): {freq_mhz}")
        self.assertAlmostEqual(freq_mhz, 6.52, places=2)

    def test_overload_frequency(self):
        breaker = Quantum_Resonance_Breaker()
        base_lambda = breaker.calculate_lambda()

        overload = Dimensional_Escape_Overload()
        overload_freq = overload.calculate_overload(base_lambda)
        print(f"Calculated Overload (MHz): {overload_freq}")
        self.assertAlmostEqual(overload_freq, 23.38, places=2)

if __name__ == '__main__':
    # Run tests and print success message if they pass
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSentez7MasterBreaker)
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    if result.wasSuccessful():
        print(f"\n{Colors.BOLD}{Colors.GREEN}[+++] MATRIX BREAKER FREQUENCY ACTIVATED [+++]{Colors.ENDC}")
        exit(0)
    else:
        exit(1)
