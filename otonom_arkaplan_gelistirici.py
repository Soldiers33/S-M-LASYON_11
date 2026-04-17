import time
import subprocess
import os

def start_autonomous_background_developer():
    print("\033[92mOTONOM ARKA PLAN GELİŞTİRİCİ BAŞLATILDI.\033[0m")
    print("Sistem arka planda simülasyonu devamlı çalıştıracak, gelişmeleri takip edecek.\n")

    iteration = 1
    while True:
        print(f"\n\033[96m=== OTONOM DÖNGÜ: İTERASYON {iteration} ===\033[0m")
        try:
            # Sınırlı çıktıyı göstermek veya arka planda çalışmasını sağlamak için subprocess
            print("Ana simülasyon (simulasyon_11.py) çalıştırılıyor...")
            result = subprocess.run(["python3", "simulasyon_11.py"], capture_output=True, text=True)
            if result.returncode == 0:
                print("\033[92mAna simülasyon başarıyla tamamlandı.\033[0m")
            else:
                print(f"\033[91mAna simülasyon hata verdi: {result.returncode}\033[0m")
                print(result.stderr[-500:]) # Sadece son hataları yazdır

            print("Doğrulama testleri (dogrulama_testleri.py) çalıştırılıyor...")
            val_result = subprocess.run(["python3", "-c", "from dogrulama_testleri import Modul_Dogrulama_Testleri; Modul_Dogrulama_Testleri().analiz()"], capture_output=True, text=True)
            if val_result.returncode == 0:
                print("\033[92mDoğrulama testleri başarıyla tamamlandı.\033[0m")

        except Exception as e:
            print(f"\033[91mOtonom Döngü Hatası: {e}\033[0m")

        print("Bir sonraki tarama döngüsü için 60 saniye bekleniyor...")
        time.sleep(60) # Arka planda yormamak için 1 dakika bekle
        iteration += 1

if __name__ == "__main__":
    start_autonomous_background_developer()
