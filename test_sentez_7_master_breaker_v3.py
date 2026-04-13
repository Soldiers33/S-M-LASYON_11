import sys
import math

try:
    from simulasyon_11 import Quantum_Resonance_Breaker, Dimensional_Escape_Overload, Pineal_Quantum_Antenna
except ImportError:
    print("ERROR: SENTEZ-7 modules not found in simulasyon_11.py")
    sys.exit(1)

def run_tests():
    print(">>> RUNNING SENTEZ-7 MASTER BREAKER TESTS <<<")

    breaker = Quantum_Resonance_Breaker()
    lambda_freq = breaker.calculate_lambda()

    escape = Dimensional_Escape_Overload()
    escape_vel = escape.calculate_escape_velocity()

    antenna = Pineal_Quantum_Antenna()
    coherence = antenna.calculate_coherence()

    print(f"Calculated Lambda Frequency (6.52 MHz expected): {lambda_freq:,.0f} Hz")
    print(f"Calculated Escape Velocity (23.38 MHz expected): {escape_vel:,.0f} Hz")
    print(f"Calculated Pineal Coherence (8.0 Hz match): {coherence:,.2f} cycles/Hz")

    # Check if lambda is ~6.52 MHz (6,521,763)
    lambda_match = abs(lambda_freq - 6521763) < 1000

    # Check if escape velocity is ~23.38 MHz (23,386,439)
    escape_match = abs(escape_vel - 23386439) < 1000

    if lambda_match and escape_match:
        print("\n[+++] MATRIX BREAKER FREQUENCY ACTIVATED [+++]")
        sys.exit(0)
    else:
        print("\n[---] FREQUENCY MISMATCH. MATRIX REMAINS INTACT. [---]")
        sys.exit(1)

if __name__ == '__main__':
    run_tests()
