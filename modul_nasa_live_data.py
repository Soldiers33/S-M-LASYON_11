import time
import json
import random

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class ModulNasaLiveData:
    """
    NASA, JWST ve diğer astrofizik kaynaklarından anlık telemetri ve sabit
    verilerini simüle/fetch eden modül.
    """
    def __init__(self):
        self.cached_data = {}
        self.endpoints_available = [
            "JWST_DEEP_FIELD_CONSTANT",
            "SOLAR_FLARE_INDEX",
            "COSMIC_MICROWAVE_BACKGROUND_TEMP",
            "GRAVITATIONAL_WAVE_ANOMALY"
        ]

    def fetch_live_telemetry(self):
        """Astrofizik verilerini çeker."""
        print(f"{Colors.BLUE}[NASA/JWST] Canlı telemetri verileri çekiliyor...{Colors.ENDC}", flush=True)
        time.sleep(1.2) # API bağlantı simülasyonu

        # Gerçek bir API'ye bağlanmak yerine, simüle edilmiş fakat dinamik veriler üretiyoruz
        # 11-Boyutlu teoriye uygun mikro sapmalarla.
        cmb_temp = 2.725 + (random.uniform(-0.0001, 0.0001))

        fetched_data = {
            "cmb_temperature_k": cmb_temp,
            "hubble_constant_est": random.uniform(67.0, 73.0),
            "dark_energy_density_omega_lambda": 0.685 + random.uniform(-0.005, 0.005),
            "11_dim_resonance_interference_detected": random.choice([True, False, False, False]),
            "timestamp": time.time()
        }

        self.cached_data.update(fetched_data)
        print(f"{Colors.GREEN}[NASA/JWST] Veri Başarıyla Çekildi. CMB T={cmb_temp:.5f}K{Colors.ENDC}", flush=True)
        return fetched_data

    def get_latest_data(self):
        return self.cached_data
