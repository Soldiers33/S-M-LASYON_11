import time
import sys
from simulasyon_11 import Simule3_Lab_V133

def autonomous_loop(max_iterations=3):
    print("\033[95m=== STARTING AUTONOMOUS BACKGROUND DEVELOPER LOOP ===\033[0m")
    for i in range(max_iterations):
        print(f"\n\033[93m[AUTONOMOUS CYCLE {i+1}/{max_iterations}]\033[0m")
        lab = Simule3_Lab_V133()
        lab.run_all()
        print("\033[92mCycle Complete. Waiting for next data stream...\033[0m")
        time.sleep(2) # Short sleep for test execution

if __name__ == '__main__':
    # Default to 1 iteration for testing, allow more in actual daemon mode
    iters = 1
    if len(sys.argv) > 1:
        iters = int(sys.argv[1])
    autonomous_loop(iters)
