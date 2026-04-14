import math
from simulasyon_11 import Quantum_Resonance_Breaker, Dimensional_Escape_Overload, Pineal_Quantum_Antenna

class MockConst:
    pass

def run_tests():
    const = MockConst()

    qr = Quantum_Resonance_Breaker(const)
    de = Dimensional_Escape_Overload(const)
    pa = Pineal_Quantum_Antenna(const)

    # 1. Test Quantum Resonance Lambda (6.52 MHz expected)
    lamb = qr.calculate_lambda()
    # 6521763 Hz based on formula

    lamb_mhz = lamb / 1000000.0

    print(f"Testing Quantum Resonance Breaker...")
    print(f"Calculated Lambda: {lamb:,.2f} Hz")

    assert math.isclose(lamb_mhz, 6.52, rel_tol=0.01), f"Expected ~6.52 MHz, got {lamb_mhz:.2f} MHz"

    # 2. Test Dimensional Escape (23.38 MHz expected)
    print(f"Testing Dimensional Escape Overload...")
    escape_mhz = de.escape_hz / 1000000.0
    assert math.isclose(escape_mhz, 23.38, rel_tol=0.01), f"Expected ~23.38 MHz, got {escape_mhz:.2f} MHz"

    # 3. Test Pineal Antenna (8.0 Hz theta to 6.52 MHz wifi)
    print(f"Testing Pineal Quantum Antenna...")
    assert pa.theta_wave == 8.0, "Expected theta wave 8.0 Hz"
    assert math.isclose(pa.universal_wifi_mhz, 6.52, rel_tol=0.01), "Expected 6.52 MHz WiFi"

    print("\n[+++] MATRIX BREAKER FREQUENCY ACTIVATED [+++]")

if __name__ == "__main__":
    run_tests()
