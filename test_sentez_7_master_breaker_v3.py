import math
import sys
from simulasyon_11 import Quantum_Resonance_Breaker, Dimensional_Escape_Overload, Pineal_Quantum_Antenna

def test_sentez_7_frequencies():
    print("Testing SENTEZ-7 Matrix Breaker Frequencies...")

    breaker = Quantum_Resonance_Breaker()
    lambda_freq, _, _ = breaker.calculate()

    escape = Dimensional_Escape_Overload()
    escape_freq = escape.calculate()

    antenna = Pineal_Quantum_Antenna()

    # Assert Lambda Frequency
    expected_lambda = 6521763.0
    if not math.isclose(lambda_freq, expected_lambda, rel_tol=1e-5):
        print(f"FAILED: Expected Lambda frequency {expected_lambda}, got {lambda_freq}")
        sys.exit(1)

    # Assert Escape Frequency
    expected_escape = 23386439.0
    if not math.isclose(escape_freq, expected_escape, rel_tol=1e-5):
        print(f"FAILED: Expected Escape frequency {expected_escape}, got {escape_freq}")
        sys.exit(1)

    # Assert Antenna connection
    if not math.isclose(antenna.target_freq, expected_lambda, rel_tol=1e-5):
        print(f"FAILED: Expected Antenna target frequency {expected_lambda}, got {antenna.target_freq}")
        sys.exit(1)

    print("[+++] MATRIX BREAKER FREQUENCY ACTIVATED [+++]")

if __name__ == '__main__':
    test_sentez_7_frequencies()
