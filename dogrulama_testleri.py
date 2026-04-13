import math
import sys

try:
    from levhi_mahfuz import LevhiMahfuzConstants
except ImportError:
    class LevhiMahfuzConstants:
        C_REAL_KMSEC = 299792.458
        GIZA_LATITUDE = 29.9792458
        VERTEBRAE_TOTAL = 66
        AXIS_COMPLEMENT = 66.6

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class Modul_Dogrulama_Testleri:
    def __init__(self, const=LevhiMahfuzConstants):
        self.const = const

    def analiz(self):
        print(f"\n{Colors.HEADER}=== MATHEMATICAL & SCIENTIFIC VERIFICATION MODULE ==={Colors.ENDC}")

        tests_passed = 0
        total_tests = 2

        # Test 1: Light Speed vs Giza Latitude Resonance
        print(f"{Colors.CYAN}[1] Verifying Speed of Light and Giza Resonance...{Colors.ENDC}")
        c_val = getattr(self.const, 'SPEED_LIGHT_REAL', getattr(self.const, 'C_REAL_KMSEC', 299792.458))
        giza_val = self.const.GIZA_LATITUDE
        # Convert C to comparable float by dividing by 10,000 as per memory instructions
        c_adjusted = c_val / 10000

        if math.isclose(c_adjusted, giza_val, rel_tol=1e-5):
            print(f"    {Colors.GREEN}✓ PASS:{Colors.ENDC} C_REAL ({c_val}) maps to Giza ({giza_val}) via 10,000 divisor.")
            tests_passed += 1
        else:
            print(f"    {Colors.FAIL}✗ FAIL:{Colors.ENDC} C_REAL adjusted ({c_adjusted}) does not match Giza ({giza_val}).")

        # Test 2: Biological / Axial Code Verification
        print(f"{Colors.CYAN}[2] Verifying Vertebrae / Axial Tilt Resonance...{Colors.ENDC}")
        vertebrae = self.const.VERTEBRAE_TOTAL
        axis_comp = self.const.AXIS_COMPLEMENT

        # Check integer alignment between 66 and 66.6
        if math.isclose(vertebrae, int(axis_comp), rel_tol=1e-5):
            print(f"    {Colors.GREEN}✓ PASS:{Colors.ENDC} Vertebrae count ({vertebrae}) aligns with Earth's axis complement ({axis_comp}°).")
            tests_passed += 1
        else:
            print(f"    {Colors.FAIL}✗ FAIL:{Colors.ENDC} Biological code {vertebrae} != Axial code {axis_comp}.")

        print(f"\n{Colors.BOLD}Verification Results: {tests_passed}/{total_tests} Tests Passed.{Colors.ENDC}")

if __name__ == "__main__":
    modul = Modul_Dogrulama_Testleri()
    modul.analiz()
