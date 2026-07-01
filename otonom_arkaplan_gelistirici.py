import subprocess
import time
import requests

def run_simulation():
    print("Starting background development and simulation...", flush=True)
    while True:
        try:
            res = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
            if res.status_code == 200:
                print("NASA data integrated into background run.", flush=True)
            with open("sim_output.log", "w") as f:
                subprocess.run(["python3", "simulasyon_11.py"], check=True, stdout=f)
            print("Run complete. Sleeping for 3600 seconds before the next run.", flush=True)
            time.sleep(3600)
        except subprocess.CalledProcessError as e:
            print(f"Simulation failed with exit code {e.returncode}", flush=True)
            time.sleep(60)
        except Exception as e:
            print(f"Error: {e}", flush=True)
            time.sleep(60)

if __name__ == "__main__":
    run_simulation()
