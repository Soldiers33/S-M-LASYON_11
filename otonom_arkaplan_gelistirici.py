import os
import time
import subprocess
import datetime
import sys

def clear_line():
    print(f"\r\033[K", end='', flush=True)

def main():
    print("\033[1m\033[95m[AUTONOMOUS BACKGROUND SIMULATION ORCHESTRATOR INITIATED]\033[0m")
    print("\033[93mTarget: Continuous execution of 11D Simulation and Data Modules\033[0m\n")

    iteration = 1
    # Run loop a fixed number of times for testing so it doesn't run infinitely in CI
    max_iterations = 3

    while iteration <= max_iterations:
        print(f"\n\033[1m\033[96m=== [OTONOM GELIŞTIRICI] ITERATION {iteration} | {datetime.datetime.now()} ===\033[0m")

        try:
            print("\033[94m>>> Executing Main Simulation (simulasyon_11.py)...\033[0m")
            # Running simulation, capturing output to avoid massive terminal spam
            # We'll show a loading bar instead.

            process = subprocess.Popen(
                [sys.executable, "simulasyon_11.py"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            # Simple loading animation while process runs
            animation = ["-", "\\", "|", "/"]
            idx = 0
            while process.poll() is None:
                print(f"\r\033[K\033[33mRunning Background Task {animation[idx % len(animation)]}\033[0m", end='', flush=True)
                idx += 1
                time.sleep(0.1)

            stdout, stderr = process.communicate()

            clear_line()

            if process.returncode == 0:
                print("\033[92m[OK] Master Simulation Cycle completed successfully.\033[0m")
                # Optional: Write logs to a file to preserve history
                with open("run_output.txt", "a") as f:
                    f.write(f"\n--- Iteration {iteration} ---\n")
                    f.write(stdout)
            else:
                print(f"\033[91m[ERROR] Master Simulation Cycle failed with return code {process.returncode}.\033[0m")
                print(f"Stderr: {stderr[:500]}...")

        except Exception as e:
            print(f"\033[91m[CRITICAL] Background orchestrator encountered an error: {str(e)}\033[0m")

        print(f"\033[93m>>> Cycle {iteration} complete. Resting before next iteration...\033[0m")
        # Sleep a short duration to prevent immediate CPU pegging, adjust as needed for real continuous running
        time.sleep(2)
        iteration += 1

    print("\n\033[1m\033[92m[AUTONOMOUS SIMULATION ORCHESTRATOR COMPLETED SCHEDULED TASKS]\033[0m")

if __name__ == "__main__":
    main()
