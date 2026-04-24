import time
import sys
from simulasyon_11 import Simule3_Lab_V133

def main():
    print("=== OTONOM ARKA PLAN GELİŞTİRİCİ BAŞLATILIYOR ===")
    print("Simülasyon arka planda sonsuz döngüde çalışacak.")

    cycle_count = 0
    while True:
        try:
            cycle_count += 1
            print(f"\n--- ARKA PLAN DÖNGÜSÜ: #{cycle_count} ---")
            lab = Simule3_Lab_V133()
            lab.run_all()
            print("\nDöngü tamamlandı. 5 saniye bekleniyor...")
            time.sleep(5)
        except Exception as e:
            print(f"Hata oluştu: {e}")
            time.sleep(10) # Hata durumunda bekle ve devam et

if __name__ == "__main__":
    main()
