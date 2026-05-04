import math
from simulasyon_11 import Simule3_Constants, Quantum_Resonance_Breaker, Dimensional_Escape_Overload

def run_tests():
    const = Simule3_Constants()
    qrb = Quantum_Resonance_Breaker(const)
    deo = Dimensional_Escape_Overload(const)

    lambda_freq = qrb.calculate_lambda()
    escape_freq = deo.check_overload()

    print(f"Testing Quantum_Resonance_Breaker...")
    print(f"Expected ~6.52 MHz, Got: {lambda_freq/1e6:.2f} MHz")

    print(f"Testing Dimensional_Escape_Overload...")
    print(f"Expected ~23.38 MHz, Got: {escape_freq/1e6:.2f} MHz")

    if math.isclose(lambda_freq/1e6, 6.52, rel_tol=0.01) and math.isclose(escape_freq/1e6, 23.38, rel_tol=0.01):
        print("\n[+++] MATRIX BREAKER FREQUENCY ACTIVATED [+++]")
        return True
    else:
        print("\n[---] MATRIX BREAKER FREQUENCY FAILED [---]")
        return False

if __name__ == "__main__":
    run_tests()
