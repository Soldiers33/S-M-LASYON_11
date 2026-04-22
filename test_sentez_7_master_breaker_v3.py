import sys
import math
from simulasyon_11 import Quantum_Resonance_Breaker, Dimensional_Escape_Overload, Pineal_Quantum_Antenna

def test_sentez_7_frequencies():
    print("Testing Quantum_Resonance_Breaker...")
    qrb = Quantum_Resonance_Breaker()
    lambda_freq, upper, lower = qrb.calculate_lambda_frequency()

    assert abs(lambda_freq - 6521763) < 10000, f"Lambda frequency {lambda_freq} is not close enough to 6.52 MHz."
    print("Quantum_Resonance_Breaker Lambda Frequency OK.")

    print("Testing Dimensional_Escape_Overload...")
    deo = Dimensional_Escape_Overload()
    escape_freq = deo.calculate_escape_frequency()

    assert escape_freq == 23386439.0, f"Escape frequency {escape_freq} does not match 23.38 MHz exactly."
    print("Dimensional_Escape_Overload Escape Frequency OK.")

    print("Testing Pineal_Quantum_Antenna...")
    pqa = Pineal_Quantum_Antenna()
    cycles = pqa.calculate_coherence()

    assert abs(cycles - (6521763.0 / 8.0)) < 1.0, f"Pineal Coherence {cycles} is incorrect."
    print("Pineal_Quantum_Antenna Coherence Cycles OK.")

    print("\n[+++] MATRIX BREAKER FREQUENCY ACTIVATED [+++]")

if __name__ == '__main__':
    test_sentez_7_frequencies()
