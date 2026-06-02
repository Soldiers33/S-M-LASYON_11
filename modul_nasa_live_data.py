import requests
import json
from datetime import datetime, timedelta

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    RED = '\033[91m'
    GOLD = '\033[33m'
    MAGENTA = '\033[35m'
    PURPLE = '\033[35m'

class ModulNasaLiveData:
    """
    NASA JPL Horizons API entegrasyonu ve canlı verilerle yepyeni 11 tabanlı formüllerin sentezlenmesi.
    """
    def __init__(self, constants=None):
        self.constants = constants
        self.live_data = {}
        self.yeni_formuller = {}
        self.base_11 = 11
        self.r11 = 11111111111
        self.ideal_moon_perigee = 363000

    def fetch_live_moon_data(self):
        """Ay'ın canlı verilerini NASA'dan çeker."""
        print(f"{Colors.CYAN}🚀 NASA JPL Horizons API Bağlantısı Kuruluyor...{Colors.ENDC}")
        try:
            today = datetime.now().strftime('%Y-%m-%d')
            tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
            url = "https://ssd.jpl.nasa.gov/api/horizons.api"
            params = {
                "format": "json",
                "COMMAND": "'301'", # Ay
                "OBJ_DATA": "'YES'",
                "MAKE_EPHEM": "'YES'",
                "EPHEM_TYPE": "'OBSERVER'",
                "CENTER": "'500@399'", # Dünya
                "START_TIME": f"'{today}'",
                "STOP_TIME": f"'{tomorrow}'",
                "STEP_SIZE": "'1 d'",
                "CSV_FORMAT": "'YES'"
            }
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                print(f"{Colors.GREEN}✅ NASA Verisi Başarıyla Çekildi.{Colors.ENDC}")
                self.live_data['moon_api_status'] = "SUCCESS"
                self.live_data['moon_response_len'] = len(response.text)
                # Parse approximate distance if available in CSV output
                lines = response.text.split('\n')
                in_data = False
                distance_km = 384400 # Default
                for line in lines:
                    if "$$SOE" in line:
                        in_data = True
                        continue
                    if "$$EOE" in line:
                        break
                    if in_data:
                        parts = [p.strip() for p in line.split(',')]
                        if len(parts) > 20: # Usually dist is column 23 or 24 depending on config, but roughly 380,000+
                            try:
                                # A very rough parsing for demonstration, real Horizons CSV is complex.
                                # Using a known value range for Earth-Moon distance (~3.6e5 to 4.0e5)
                                for p in parts:
                                    try:
                                        val = float(p)
                                        if 350000 < val < 410000:
                                            distance_km = val
                                            break
                                    except:
                                        pass
                            except:
                                pass
                self.live_data['current_moon_distance_km'] = distance_km
            else:
                print(f"{Colors.FAIL}❌ NASA API Hatası: HTTP {response.status_code}{Colors.ENDC}")
                self.live_data['moon_api_status'] = "FAILED"
                self.live_data['current_moon_distance_km'] = 384400 # Default mean
        except Exception as e:
            print(f"{Colors.FAIL}❌ NASA API Bağlantı Hatası: {e}{Colors.ENDC}")
            self.live_data['moon_api_status'] = "ERROR"
            self.live_data['current_moon_distance_km'] = 384400

    def sentez_yeni_formuller(self):
        """NASA canlı verisi ile 11 sisteminin yeni sentezi"""
        print(f"{Colors.MAGENTA}🔮 NASA Verisi ile Yeni 11-Boyutlu Formüller Sentezleniyor...{Colors.ENDC}")
        dist = self.live_data.get('current_moon_distance_km', 384400)

        # SENTEZ 1: CANLI AY-HATAY REZONANSI
        hatay_lat = 36.3
        rezonans_oran = dist / hatay_lat
        sapma_11 = abs(rezonans_oran - (self.ideal_moon_perigee / hatay_lat))

        self.yeni_formuller['canli_ay_rezonans'] = {
            'oran': rezonans_oran,
            'sapma_11_sistemi': sapma_11,
            'aciklama': "Canlı Ay mesafesinin Hatay enlemine bölümü"
        }

        # SENTEZ 2: KUANTUM ÇEKİM DALGALANMASI (11 TABANLI)
        # G_ideal = 6.666e-11
        # Dalgalanma = (dist / ideal_moon) * G_ideal
        g_ideal = 6.666e-11
        dalgalanma = (dist / self.ideal_moon_perigee) * g_ideal

        self.yeni_formuller['kuantum_cekim_dalga'] = {
            'dalga_degeri': dalgalanma,
            'kuantum_kati': dalgalanma / g_ideal,
            'aciklama': "Canlı Ay mesafesine göre Kuantum Çekim Dalgalanması"
        }

        # SENTEZ 3: R11 KOZMİK BAĞ
        # Canlı mesafe ile R11 (11111111111) ilişkisi
        r11_bag = self.r11 / dist

        self.yeni_formuller['r11_kozmik_bag'] = {
            'bag_katsayisi': r11_bag,
            'aciklama': "R11'in Canlı Ay mesafesine oranı"
        }

        print(f"  ✓ Canlı Rezonans Oranı: {rezonans_oran:.2f}")
        print(f"  ✓ Kuantum Dalgalanma Katı: {dalgalanma/g_ideal:.5f}")
        print(f"  ✓ R11 Bağ Katsayısı: {r11_bag:.2f}")

    def analiz(self):
        """Tüm NASA modül analizini çalıştırır ve verileri döndürür."""
        print(f"\n{Colors.BOLD}{Colors.GOLD}--- NASA CANLI VERİ & YENİ SENTEZ MODÜLÜ ---{Colors.ENDC}")
        self.fetch_live_moon_data()
        self.sentez_yeni_formuller()
        print(f"{Colors.BOLD}{Colors.GREEN}--- MODÜL TAMAMLANDI ---{Colors.ENDC}\n")

        return {
            'nasa_live': self.live_data,
            'yeni_formuller': self.yeni_formuller
        }

if __name__ == "__main__":
    modul = ModulNasaLiveData()
    modul.analiz()
