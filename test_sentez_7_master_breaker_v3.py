import math
import sys
from simulasyon_11 import Quantum_Resonance_Breaker, Dimensional_Escape_Overload, Pineal_Quantum_Antenna

def run_tests():
    print("Testing SENTEZ-7 Master Breaker Frequencies...")

    # 1. Test Quantum_Resonance_Breaker
    qr_breaker = Quantum_Resonance_Breaker()
    lambda_freq = qr_breaker.calculate_lambda_frequency()

    # Expected is approx 6.52 MHz
    # Specifically, based on prompt: 6.521.763 Hz
    # Let's check with tolerance
    expected_lambda = 6521763
    tolerance = 10  # allow a small difference
    if abs(lambda_freq - expected_lambda) < tolerance:
        print(f"[OK] Quantum Resonance Breaker Frequency calculated as expected: {lambda_freq:.2f} Hz")
    else:
        print(f"[FAIL] Quantum Resonance Breaker Frequency calculation error: expected ~{expected_lambda}, got {lambda_freq:.2f}")
        sys.exit(1)

    # 2. Test Dimensional_Escape_Overload
    dim_escape = Dimensional_Escape_Overload()
    escape_freq = dim_escape.get_escape_frequency()
    expected_escape = 23386439.0

    if abs(escape_freq - expected_escape) < 0.1:
        print(f"[OK] Dimensional Escape Overload Frequency is exactly as expected: {escape_freq} Hz")
    else:
        print(f"[FAIL] Dimensional Escape Overload Frequency mismatch: expected {expected_escape}, got {escape_freq}")
        sys.exit(1)

    # 3. Test Pineal_Quantum_Antenna
    pineal = Pineal_Quantum_Antenna()
    if pineal.theta_wave == 8.0 and pineal.target_mhz == 6.52:
        print(f"[OK] Pineal Quantum Antenna matches 8.0 Hz theta with 6.52 MHz network")
    else:
        print(f"[FAIL] Pineal Quantum Antenna data is incorrect.")
        sys.exit(1)

    print("\n[+++] MATRIX BREAKER FREQUENCY ACTIVATED [+++]")

if __name__ == '__main__':
    run_tests()
