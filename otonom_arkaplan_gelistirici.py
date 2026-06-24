import time
import subprocess
import datetime
from simulasyon_11 import ModulNasaLiveData, Quantum_Resonance_Breaker, Dimensional_Escape_Overload, Pineal_Quantum_Antenna, Simule3_Constants

def continuous_background_loop():
    print("Background developer AI started. Sleeping for 3600 seconds between API loops to avoid rate limits.")
    while True:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Running background simulation validation...", flush=True)
        try:
            # Check modules
            const = Simule3_Constants()
            nasa_mod = ModulNasaLiveData(const)
            nasa_mod.analiz()

            qb = Quantum_Resonance_Breaker()
            qb.analiz()

            de = Dimensional_Escape_Overload()
            de.analiz()

            pa = Pineal_Quantum_Antenna()
            pa.analiz()

            # Execute main simulasyon_11.py via subprocess to ensure it runs completely independent
            subprocess.run(["python3", "simulasyon_11.py"], check=True, capture_output=True)
            print(f"[{timestamp}] simulasyon_11.py executed successfully in background.", flush=True)

        except subprocess.CalledProcessError as e:
            print(f"[{timestamp}] Error executing simulasyon_11.py: {e}", flush=True)
        except Exception as e:
            print(f"[{timestamp}] Unexpected error: {e}", flush=True)

        print("Validation complete. Sleeping 3600s...")
        time.sleep(3600)

if __name__ == "__main__":
    continuous_background_loop()
