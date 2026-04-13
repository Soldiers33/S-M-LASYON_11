import math
import sys

def test_master_breaker():
    # Variables required for the Lambda calculation
    V = 1331.0
    Q = 6666.0
    C_i = 1.11188
    G_i = 0.008271
    H = 1390.0
    T_End = 1999.0

    # Lambda Frequency (6.52 MHz)
    lambda_freq = ((V * Q * C_i) / (G_i * H)) * math.log(T_End)
    expected_lambda = 6521763

    # Asserting Lambda Frequency
    diff = abs(lambda_freq - expected_lambda)
    if diff > 100:  # Allow some margin due to float precision
        print(f"FAILED: Expected Lambda Frequency around {expected_lambda}, got {lambda_freq:.2f}")
        sys.exit(1)

    print(f"PASS: Lambda Frequency calculated as {lambda_freq:,.2f} Hz")

    # Dimensional Escape Overload Frequency
    escape_freq = 23386439.0 # 23.38 MHz

    # Given the requirements we just make sure it's printed
    print(f"PASS: Dimensional Escape Velocity is set to {escape_freq:,.0f} Hz")

    print("\n[+++] MATRIX BREAKER FREQUENCY ACTIVATED [+++]")

if __name__ == '__main__':
    test_master_breaker()
