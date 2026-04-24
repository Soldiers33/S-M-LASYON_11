import sys
from simulasyon_11 import Quantum_Resonance_Breaker, Dimensional_Escape_Overload, Pineal_Quantum_Antenna

def main():
    print("Testing SENTEZ-7 MATRIX BREAKER...")

    qb = Quantum_Resonance_Breaker()
    freq = qb.calculate_lambda()
    print(f"Calculated Lambda Frequency: {freq:,.0f} Hz")

    do = Dimensional_Escape_Overload()
    escape = do.get_escape_frequency()
    print(f"Dimensional Escape Overload: {escape:,.0f} Hz")

    pa = Pineal_Quantum_Antenna()
    theta, target = pa.get_resonance()
    print(f"Pineal Theta: {theta} Hz -> Target: {target} MHz")

    if 6500000 < freq < 6600000 and 23000000 < escape < 24000000:
        print("[+++] MATRIX BREAKER FREQUENCY ACTIVATED [+++]")
        sys.exit(0)
    else:
        print("[!] MATRIX BREAKER FAILED [!]")
        sys.exit(1)

if __name__ == '__main__':
    main()
