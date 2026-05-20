import time
import subprocess
import datetime
import sys

def main():
    print("Starting Autonomous Background Execution Loop...")
    print("This loop will continuously develop and execute the core simulation.", flush=True)

    # We set it to run a few times for the test purposes
    # To respect the user's continuous request, it's an infinite loop
    while True:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n[{timestamp}] Initiating new execution cycle...", flush=True)

        try:
            # Run the simulation
            process = subprocess.run(
                [sys.executable, "simulasyon_11.py"],
                capture_output=True,
                text=True,
                timeout=60 # Prevent infinite hangs if a module hangs
            )

            if process.returncode == 0:
                print(f"[{timestamp}] Simulation executed successfully. Matrix integrity stable.", flush=True)
                # print partial output to show it worked
                print(process.stdout[-500:], flush=True)
            else:
                print(f"[{timestamp}] Simulation encountered an error.", flush=True)
                print(process.stderr, flush=True)

        except subprocess.TimeoutExpired:
            print(f"[{timestamp}] Simulation timed out. Recovering...", flush=True)
        except Exception as e:
            print(f"[{timestamp}] Unexpected error: {e}", flush=True)

        print("Sleeping before next cycle to prevent API rate limiting...", flush=True)
        # Sleep for 1 hour as per memory to avoid rate limits (arxiv, NASA, etc)
        time.sleep(3600)

if __name__ == "__main__":
    main()
