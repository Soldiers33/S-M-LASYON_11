import time
import subprocess
from datetime import datetime
from modul_nasa_live_data import ModulNasaLiveData

print("Starting Autonomous Background Developer Loop...")
nasa_module = ModulNasaLiveData()

while True:
    print(f"\n--- BACKGROUND CYCLE START: {datetime.now()} ---", flush=True)

    print("Running NASA & AI Verification fetch...", flush=True)
    try:
        nasa_module.analiz()
    except Exception as e:
        print(f"Error fetching data: {e}", flush=True)

    print("Running theoretical background tests...", flush=True)
    try:
        # Run some lightweight validation
        subprocess.run(["python3", "test_11_dimensional_constants.py"], capture_output=True, text=True, check=True)
        print("Theoretical background tests completed.", flush=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running tests. Exit status: {e.returncode}", flush=True)
    except Exception as e:
        print(f"Error running tests: {e}", flush=True)

    print("Cycle complete. Sleeping for 3600 seconds to respect API limits...", flush=True)
    # The user specifically requested a continuous background loop, so we do not break.
    time.sleep(3600)
