import time
import subprocess
import os

print("Starting Autonomous Background Developer...")
with open("otonom_arkaplan.log", "a") as log_file:
    log_file.write(f"Started at {time.ctime()}\n")

while True:
    try:
        # Run tests and simulations
        result = subprocess.run(["python3", "simulasyon_11.py"], capture_output=True, text=True, check=True)
        with open("otonom_arkaplan.log", "a") as log_file:
            log_file.write(f"[{time.ctime()}] Simulation ran successfully.\n")
    except subprocess.CalledProcessError as e:
        with open("otonom_arkaplan.log", "a") as log_file:
            log_file.write(f"[{time.ctime()}] Simulation failed with status {e.returncode}.\n")
            log_file.write(e.output + "\n")
            log_file.flush()
    except Exception as e:
        with open("otonom_arkaplan.log", "a") as log_file:
            log_file.write(f"[{time.ctime()}] Error: {str(e)}\n")
            log_file.flush()

    # Sleep for a significant duration to prevent API rate limiting (e.g. 1 hour)
    time.sleep(3600)
