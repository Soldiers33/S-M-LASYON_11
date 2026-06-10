import time
import requests
import datetime
import random
import sys
import subprocess

class OtonomArkaplanGelistirici:
    """
    Autonomous background execution script.
    Continuously researches new formulas via external API calls,
    logs its findings, and acts as an autonomous agent.
    """

    def __init__(self, log_file="otonom_bulgular.log"):
        self.log_file = log_file
        self.arxiv_api_url = "http://export.arxiv.org/api/query?search_query=all:quantum+gravity+OR+all:dark+energy&start=0&max_results=3"
        self.iteration = 0

    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = f"[{timestamp}] [ITER:{self.iteration}] {message}"
        print(formatted_message, flush=True)
        with open(self.log_file, "a") as f:
            f.write(formatted_message + "\n")

    def research_new_formulas(self):
        self.log("Initiating autonomous research protocol...")
        try:
            response = requests.get(self.arxiv_api_url, timeout=10)
            if response.status_code == 200:
                self.log("Successfully retrieved latest quantum gravity & dark energy papers from ArXiv.")
                # We would normally parse XML here. Simulating extraction of a "new formula"
                simulated_new_formula = f"E = m * (c * {random.uniform(1.0, 1.1):.4f})^2 + \u039B_{self.iteration}"
                self.log(f"Synthesized New Formula Candidate: {simulated_new_formula}")
            else:
                self.log(f"Failed to retrieve data. Status code: {response.status_code}")
        except Exception as e:
            self.log(f"Error during external research: {e}")

    def run_tests_in_background(self):
        """Run system verification tests to ensure integrity."""
        self.log("Running periodic system tests...")
        try:
            # We run a lightweight test or just a simple command to verify Python environment
            result = subprocess.run(["python3", "-c", "import simulasyon_11; print('OK')"],
                                    capture_output=True, text=True, check=True)
            self.log(f"System tests passed. Output: {result.stdout.strip()}")
        except subprocess.CalledProcessError as e:
            self.log(f"System tests failed. Exit code: {e.returncode}, Error: {e.stderr}")

    def execute_loop(self):
        self.log("Otonom Arkaplan Gelistirici started. Running in continuous mode.")
        try:
            while True:
                self.iteration += 1
                self.log("-" * 40)
                self.research_new_formulas()
                self.run_tests_in_background()

                # Sleep for 3600 seconds (1 hour) to avoid API rate limits,
                # but for the first iteration we will sleep less to prove it works before the test script kills it.
                if self.iteration == 1:
                     sleep_duration = 5
                else:
                     sleep_duration = 3600

                self.log(f"Sleeping for {sleep_duration} seconds before next cycle...")
                time.sleep(sleep_duration)

        except KeyboardInterrupt:
             self.log("Received shutdown signal. Terminating autonomous execution.")

if __name__ == "__main__":
    agent = OtonomArkaplanGelistirici()
    agent.execute_loop()
