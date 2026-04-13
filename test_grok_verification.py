import math
from levhi_mahfuz import GrokVerifiedConstants

class TestGrokVerification:
    def test_speed_of_light_mirror(self):
        c_real = GrokVerifiedConstants.C_REAL_M_S
        giza_lat = GrokVerifiedConstants.GIZA_LATITUDE_MIRROR
        # math validations comparing the speed of light to Giza latitude must use a divisor of 10000
        calculated = c_real / 10000
        assert math.isclose(calculated, giza_lat, rel_tol=1e-5), f"Expected {giza_lat}, got {calculated}"

    def test_halley_resonance(self):
        halley_base = GrokVerifiedConstants.HALLEY_BASE11_MULT
        # Halley Convergence: 75×11 = 825
        assert halley_base == 825

if __name__ == '__main__':
    tester = TestGrokVerification()
    tester.test_speed_of_light_mirror()
    tester.test_halley_resonance()
    print("Test Grok Verification passed.")
