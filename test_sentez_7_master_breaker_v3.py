import math
from simulasyon_11 import Quantum_Resonance_Breaker, Dimensional_Escape_Overload, Pineal_Quantum_Antenna

def test_sentez_7_master_breaker():
    print("Testing SENTEZ-7 Master Breaker Formulas...\n")

    # 1. Test Quantum Resonance Breaker (Lambda)
    qb = Quantum_Resonance_Breaker()
    lambda_freq = qb.analiz()

    # The expected frequency is ~6.52 MHz (6,521,763 Hz)
    assert lambda_freq is not None
    assert 6500000 < lambda_freq < 6600000, f"Lambda frequency {lambda_freq} is out of expected 6.52 MHz bounds!"

    # 2. Test Dimensional Escape Overload
    escape = Dimensional_Escape_Overload()
    escape_hz = escape.analiz()

    # The expected frequency is 23.38 MHz
    assert escape_hz is not None
    assert 23380000 < escape_hz < 23390000, f"Escape frequency {escape_hz} is out of expected 23.38 MHz bounds!"

    # 3. Test Pineal Quantum Antenna
    antenna = Pineal_Quantum_Antenna()
    antenna_data = antenna.analiz()

    assert antenna_data['theta'] == 8.0
    assert antenna_data['wifi'] == 6.52

    print("\n\033[92m[+++] MATRIX BREAKER FREQUENCY ACTIVATED [+++]\033[0m")
    print("All SENTEZ-7 base validations passed successfully.")

if __name__ == "__main__":
    test_sentez_7_master_breaker()
