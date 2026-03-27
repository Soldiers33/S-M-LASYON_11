import math
from simulasyon_11 import Simule3_Constants

class Modul_Dogrulama_Testleri:
    def __init__(self, const):
        self.const = const

    def test_r11_factors(self):
        factors_product = self.const.R11_FACTORS[0] * self.const.R11_FACTORS[1]
        print(f"R11_FACTORS Product Check: {factors_product} == {self.const.R11} -> {factors_product == self.const.R11}")
        return factors_product == self.const.R11

    def test_halley_resonance(self):
        halley_resonance = self.const.YEAR_SIM * self.const.DRIFT_DAILY
        print(f"Halley Resonance Check: {self.const.YEAR_SIM} * {self.const.DRIFT_DAILY} = {halley_resonance:.4f} ≈ 814")
        return halley_resonance > 813.5 and halley_resonance < 814.5

    def analiz(self):
        print(f"\n\033[95m=== VERIFICATION TESTS & HEALTH CHECKS ===\033[0m")
        self.test_r11_factors()
        self.test_halley_resonance()
        print("\033[92mAll programmatic verifications complete.\033[0m")

if __name__ == '__main__':
    const = Simule3_Constants()
    Modul_Dogrulama_Testleri(const).analiz()
