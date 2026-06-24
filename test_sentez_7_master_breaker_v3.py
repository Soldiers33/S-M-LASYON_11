from simulasyon_11 import Quantum_Resonance_Breaker, Dimensional_Escape_Overload, Colors

def run_tests():
    print(f"{Colors.BOLD}{Colors.CYAN}--- RUNNING SENTEZ-7 MASTER BREAKER TESTS ---{Colors.ENDC}")

    qb = Quantum_Resonance_Breaker()
    lambda_val = qb.calculate_lambda()
    print(f"Calculated Lambda: {lambda_val:.2f} Hz")

    de = Dimensional_Escape_Overload()
    escape_val = de.check_overload()
    print(f"Escape Velocity: {escape_val} Hz")

    if abs(lambda_val - 6521763) < 1000 and abs(escape_val - 23386439) < 10:
        print(f"\\n{Colors.BOLD}{Colors.GREEN}[+++] MATRIX BREAKER FREQUENCY ACTIVATED [+++]{Colors.ENDC}")
    else:
        print(f"\\n{Colors.BOLD}{Colors.RED}[FAIL] Frequencies do not match expectations.{Colors.ENDC}")

if __name__ == "__main__":
    run_tests()
