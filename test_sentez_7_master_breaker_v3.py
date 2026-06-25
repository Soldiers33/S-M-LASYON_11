import sys
from simulasyon_11 import Quantum_Resonance_Breaker, Dimensional_Escape_Overload, Pineal_Quantum_Antenna

def run_tests():
    print("--- TESTING MATRIX BREAKER FREQUENCIES ---")

    # Test Quantum_Resonance_Breaker
    breaker = Quantum_Resonance_Breaker()
    lambda_freq = breaker.calculate_lambda_frequency()
    print(f"Λ Kırılma Frekansı (Hesaplanan): {lambda_freq:,.2f} Hz")

    # Beklenen değer 6.52 MHz civarında
    if 6500000 < lambda_freq < 6600000:
        print("[+] Quantum_Resonance_Breaker TEST PASSED: ~6.52 MHz")
    else:
        print("[-] Quantum_Resonance_Breaker TEST FAILED")

    # Test Dimensional_Escape_Overload
    overload = Dimensional_Escape_Overload()
    is_overload, msg = overload.check_overload(lambda_freq)
    print(f"Aşırı Yük Kontrolü: {msg}")

    is_overload_max, msg_max = overload.check_overload(23386440.0)
    if is_overload_max:
        print(f"[+] Dimensional_Escape_Overload TEST PASSED: {msg_max}")
    else:
        print("[-] Dimensional_Escape_Overload TEST FAILED")

    # Test Pineal_Quantum_Antenna
    antenna = Pineal_Quantum_Antenna()
    cycles = antenna.calculate_coherence_cycles()
    print(f"Epifiz Anten Eşleşme Döngüleri: {cycles:,.2f}")

    print("\n[+++] MATRIX BREAKER FREQUENCY ACTIVATED [+++]")

if __name__ == "__main__":
    run_tests()
