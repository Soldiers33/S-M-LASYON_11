import math
from simulasyon_11 import Quantum_Resonance_Breaker, Dimensional_Escape_Overload, Pineal_Quantum_Antenna

def run_tests():
    breaker = Quantum_Resonance_Breaker()
    freq = breaker.calculate_lambda()

    # 6.52 MHz ~ 6521763 Hz
    assert abs(freq - 6521763) < 1.0, f"Expected ~6521763, got {freq}"

    escape = Dimensional_Escape_Overload()
    assert escape.escape_freq == 23386439.0, f"Expected 23386439.0, got {escape.escape_freq}"

    pineal = Pineal_Quantum_Antenna()
    assert pineal.theta_hz == 8.0, "Expected theta 8.0"
    assert pineal.universal_wifi_mhz == 6.52, "Expected 6.52 MHz WiFi"

    print("[+++] MATRIX BREAKER FREQUENCY ACTIVATED [+++]")

if __name__ == "__main__":
    run_tests()
