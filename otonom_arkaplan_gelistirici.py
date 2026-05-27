import time
import datetime
from modul_nasa_live_data import Modul_NASA_LiveData
from deep_research_module import DeepResearchModule
import dogrulama_testleri as Yeni_Dogrulama

def main():
    print("================================================================================", flush=True)
    print("AUTONOMOUS BACKGROUND DEVELOPER STARTING...", flush=True)
    print("================================================================================", flush=True)

    nasa_module = Modul_NASA_LiveData()
    arxiv_module = DeepResearchModule()

    while True:
        try:
            print(f"\n[{datetime.datetime.now()}] Waking up to fetch data...", flush=True)
            validation_queue = Yeni_Dogrulama.DogrulamaTestleri()

            # Fetch NASA data
            nasa_results = nasa_module.analiz()
            if nasa_results:
                for k, v in nasa_results.items():
                    validation_queue.add_to_queue("NASA", "Astronomical", v, k)

            # Fetch arXiv data
            arxiv_results = arxiv_module.analiz()
            if arxiv_results:
                for k, v in arxiv_results.items():
                    validation_queue.add_to_queue("arXiv", "Quantum/String", v, k)

            # Run validation
            validation_queue.run_all_validations()

            # Sleep for an hour (3600 seconds) to avoid rate limiting
            print(f"[{datetime.datetime.now()}] Sleeping for 3600 seconds...", flush=True)
            time.sleep(3600)

        except Exception as e:
            print(f"[{datetime.datetime.now()}] Error occurred: {e}", flush=True)
            time.sleep(600) # Sleep 10 minutes on error before retry

if __name__ == "__main__":
    main()
