import time
import subprocess
import datetime

class Autonomous_Background_Dev:
    def __init__(self):
        self.iteration = 0
        self.run_interval = 10 # seconds (for testing, make it fast, usually would be hours)

    def run(self, max_iterations=1):
        print("\n\033[1m\033[93m[OTONOM SİSTEM BAŞLATILDI] - Arka planda geliştirme ve çalıştırma döngüsü aktif.\033[0m")
        while self.iteration < max_iterations:
            self.iteration += 1
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"\n[{now}] === OTONOM DÖNGÜ: İTERASYON {self.iteration} ===")

            # Here we would normally run the simulation or tests.
            print("Arka planda simülasyon çalıştırılıyor (simulasyon_11.py)...")

            # Using subprocess to run the simulation
            try:
                # Use a brief test script just to show it works, or we can actually run the main script.
                # Running the main script could produce too much output, so we redirect it.
                with open("run_output.txt", "w") as f:
                    subprocess.run(["python3", "simulasyon_11.py"], stdout=f, stderr=subprocess.STDOUT)
                print("[\033[92mOK\033[0m] Simülasyon başarıyla tamamlandı. Sonuçlar 'run_output.txt' dosyasına kaydedildi.")
            except Exception as e:
                print(f"[\033[91mHATA\033[0m] Simülasyon çalıştırılırken hata: {e}")

            if self.iteration < max_iterations:
                print(f"{self.run_interval} saniye bekleniyor...")
                time.sleep(self.run_interval)

        print("\n\033[1m\033[93m[OTONOM SİSTEM DURDURULDU] - Döngü tamamlandı.\033[0m")

if __name__ == "__main__":
    Autonomous_Background_Dev().run(max_iterations=1)
