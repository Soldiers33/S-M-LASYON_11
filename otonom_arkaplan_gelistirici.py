#!/usr/bin/env python3
import subprocess
import time

def run_simulation():
    try:
        subprocess.run(["python3", "simulasyon_11.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running simulation: {e}")

if __name__ == "__main__":
    print("Starting background development and execution...")
    while True:
        run_simulation()
        time.sleep(10) # 10 seconds delay
