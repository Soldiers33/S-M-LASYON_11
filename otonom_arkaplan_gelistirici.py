import time
import subprocess
import traceback
from datetime import datetime

def background_task():
    print(f"[{datetime.now().isoformat()}] Otonom Arkaplan Gelistirici baslatiliyor...", flush=True)

    while True:
        try:
            print(f"\n[{datetime.now().isoformat()}] Yeni NASA/ArXiv verileri taraniyor...", flush=True)

            # Using the newly created module to fetch data
            from modul_nasa_live_data import ModulNasaLiveData
            from dogrulama_testleri import DogrulamaTestleri

            nasa_module = ModulNasaLiveData()
            dogrulama = DogrulamaTestleri()

            res = nasa_module.fetch_jwst_data()
            print(f"[{datetime.now().isoformat()}] NASA Data Check Result: {res}", flush=True)

            if res.get("status") == "success":
                dogrulama.add_to_queue(res)
                dogrulama.run_integrity_checks()

            print(f"[{datetime.now().isoformat()}] Otonom gelistirme dongusu tamamlandi. 1 saat uyku moduna geciliyor...", flush=True)
        except Exception as e:
            print(f"[{datetime.now().isoformat()}] Hata olustu: {e}", flush=True)
            traceback.print_exc()

        # Significant sleep to prevent API rate limits (1 hour)
        time.sleep(3600)

if __name__ == "__main__":
    background_task()
