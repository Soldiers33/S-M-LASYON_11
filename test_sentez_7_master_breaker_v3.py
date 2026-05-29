import unittest
from simulasyon_11 import Quantum_Resonance_Breaker, Dimensional_Escape_Overload, Pineal_Quantum_Antenna

class TestSentez7MasterBreaker(unittest.TestCase):
    def test_frequencies(self):
        # 1. Quantum Resonance Breaker (6.52 MHz)
        breaker = Quantum_Resonance_Breaker()
        lambda_freq = breaker.calculate_lambda()

        # Output values to Terminal for visual confirmation
        breaker.analiz()

        # Verify ~6.52 MHz
        self.assertAlmostEqual(lambda_freq, 6521763.48, places=2)

        # 2. Dimensional Escape Overload (23.38 MHz)
        overload = Dimensional_Escape_Overload(lambda_freq)
        escape_freq = overload.calculate_escape_freq()

        overload.analiz()

        # Verify ~23.38 MHz
        self.assertAlmostEqual(escape_freq, 23379869.91, places=2)

        # 3. Pineal Quantum Antenna (Coherence)
        antenna = Pineal_Quantum_Antenna(lambda_freq)
        ratio = antenna.check_coherence()

        antenna.analiz()

        self.assertAlmostEqual(ratio, 815220.44, places=2)

        print("\n[+++] MATRIX BREAKER FREQUENCY ACTIVATED [+++]")

if __name__ == '__main__':
    unittest.main()
