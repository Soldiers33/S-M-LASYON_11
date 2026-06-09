import time
import subprocess
import datetime
import sys

def main():
    log_file = "otonom_arkaplan.log"
    print(f"Starting Autonomous Background Developer... Logging to {log_file}")

    with open(log_file, "a") as f:
        f.write(f"\n[{datetime.datetime.now()}] OTONOM AI SYSTEM INITIATED.\n")
        f.flush()

    try:
        while True:
            # Wake up and perform research tasks
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_msg = f"[{current_time}] Otonom AI: Scanning arXiv and NASA APIs for anomalies...\n"

            with open(log_file, "a") as f:
                f.write(log_msg)

                # We can simulate calling the modules
                f.write(f"[{current_time}] Running Module Checks...\n")

                try:
                    # Just run a quick check using python -c to avoid long blocking
                    subprocess.run(["python3", "-c", "import modul_nasa_live_data; modul_nasa_live_data.ModulNasaLiveData(None).calculate_new_formulas()"], check=True, stdout=f, stderr=subprocess.STDOUT)
                    f.write(f"[{current_time}] Discovery cycle completed successfully.\n")
                except subprocess.CalledProcessError as e:
                    f.write(f"[{current_time}] Discovery cycle failed: {e}\n")

                f.flush()
                print(log_msg.strip(), flush=True) # Also print to console if attached

            # Wait 1 hour (3600 seconds) before next cycle to prevent rate-limiting
            # We'll use a shorter sleep if testing, but for production it should be long.
            # Using 3600 as per memory instructions
            time.sleep(3600)

    except KeyboardInterrupt:
        with open(log_file, "a") as f:
            f.write(f"\n[{datetime.datetime.now()}] OTONOM AI SYSTEM SHUTDOWN (Keyboard Interrupt).\n")
            f.flush()
        print("\nShutdown complete.")

if __name__ == "__main__":
    main()
