import sys
from simulasyon_11 import Quantum_Resonance_Breaker, Dimensional_Escape_Overload

def test_sentez_7():
    breaker = Quantum_Resonance_Breaker()
    escape = Dimensional_Escape_Overload()

    val_breaker = breaker.calculate_lambda()
    val_escape = escape.escape_freq

    print(f"Testing Quantum Resonance Breaker Lambda: {val_breaker:,.0f} Hz")
    print(f"Testing Dimensional Escape Overload Frequency: {val_escape:,.0f} Hz")

    # 6.52 MHz is approximately 6,521,763 Hz
    assert round(val_breaker / 1e6, 2) == 6.52, f"Expected ~6.52 MHz, got {val_breaker/1e6:.2f} MHz"
    assert round(val_escape / 1e6, 2) == 23.38, f"Expected ~23.38 MHz, got {val_escape/1e6:.2f} MHz"

    print("\n[+++] MATRIX BREAKER FREQUENCY ACTIVATED [+++]")
    print("All tests passed successfully.")

if __name__ == "__main__":
    test_sentez_7()
