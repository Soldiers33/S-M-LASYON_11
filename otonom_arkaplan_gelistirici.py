import time
from simulasyon_11 import Simule3_Lab_V133, Colors

def main():
    print(f"{Colors.GREEN}================================================================================{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.CYAN}  OTONOM ARKA PLAN GELİSTİRİCİ - 11 BOYUTLU SİMÜLASYON SÜREKLİ ÇALIŞMA DÖNGÜSÜ{Colors.ENDC}")
    print(f"{Colors.GREEN}================================================================================{Colors.ENDC}")
    print("Sistem, sen yokken de arka planda veri toplayacak ve simülasyonu geliştirecektir.\n")

    loop_count = 1
    while True:
        try:
            print(f"\n{Colors.BOLD}{Colors.MAGENTA}>>> DÖNGÜ BAŞLIYOR: {loop_count} <<<{Colors.ENDC}")
            sim_lab = Simule3_Lab_V133()
            sim_lab.run_all()
            print(f"\n{Colors.GREEN}>>> DÖNGÜ {loop_count} TAMAMLANDI. BİR SONRAKİ İTERASYON BEKLENİYOR... <<<{Colors.ENDC}")
            loop_count += 1

            # Sleep to prevent high CPU usage, simulating long-running periodic tasks
            time.sleep(10)


        except Exception as e:
            print(f"{Colors.FAIL}Error in autonomous loop: {e}{Colors.ENDC}")
            time.sleep(5)

if __name__ == "__main__":
    main()
