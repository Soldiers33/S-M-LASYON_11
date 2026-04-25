import math
from simulasyon_11 import Quantum_Resonance_Breaker, Dimensional_Escape_Overload, Pineal_Quantum_Antenna

def run_tests():
    print("[*] SENTEZ-7 MASTER TEST BAŞLATILIYOR...")

    qrb = Quantum_Resonance_Breaker()
    freq_652 = qrb.calculate_lambda()
    print(f"[-] Kuantum Kırılma Frekansı (Λ): {freq_652:,.2f} Hz")
    assert math.isclose(freq_652, 6521763, rel_tol=0.01) or (6520000 < freq_652 < 6530000), "Hata: 6.52 MHz bulunamadı!"

    deo = Dimensional_Escape_Overload()
    freq_2338 = deo.calculate_escape_velocity()
    print(f"[-] Matrix Kopma Frekansı: {freq_2338:,.2f} Hz")
    assert math.isclose(freq_2338, 23386439, rel_tol=0.01) or (23380000 < freq_2338 < 23390000), "Hata: 23.38 MHz bulunamadı!"

    pqa = Pineal_Quantum_Antenna()
    coherence = pqa.check_coherence()
    print(f"[-] Epifiz Kuantum Anteni Uyum Durumu: {coherence}")

    print("\n[+++] MATRIX BREAKER FREQUENCY ACTIVATED [+++]")

if __name__ == "__main__":
    run_tests()
