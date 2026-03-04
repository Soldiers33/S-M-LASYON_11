# UV Quick Start Guide - S-M-LASYON_11 Projesi

## 🌟 UV Nedir?

UV (Astral's Universal Virtualenv), Python paketlerini yönetmek ve Python scriptlerini çalıştırmak için tasarlanmış ultra hızlı bir araçtır.

**Avantajları:**
- ⚡ Pip'den 10-100x daha hızlı
- 📦 Otomatik venv yönetimi (sanal ortam oluşturma gerekmez)
- 🔒 Reproducible çalışmalar (deterministic dependency resolution)
- 🎯 Proje başına konfigürasyon (pyproject.toml)

---

## ✅ Kurulum Kontrol

UV başarıyla kurulduysa, aşağıdaki komutlar çalışmalır:

```bash
uv --version        # UV sürümünü göster
uv --help           # Yardım menüsü
uvx --version       # UVEX sürümünü göster
```

**Beklenen Çıktı:**
```
uv 0.10.8 (x86_64-unknown-linux-gnu)
```

---

## 🚀 Temel Komutlar

### 1. Python Script Çalıştır (Otomatik Venv ile)

```bash
# Basit script çalıştır
uv run simulasyon_11.py

# Parametrelerle çalıştır
uv run simulasyon_11.py --iterations 50000

# Test dosyası çalıştır
uv run test_11_dimensional_constants.py

# Monte Carlo runner (KAR TOPU V5 doğrulama)
uv run uv_monte_carlo_runner.py
```

### 2. Paket Yükleme (Anda gerekirse)

```bash
# Başarılı bir şekilde yükleme (package.json gibi)
uv pip install numpy pandas scipy flask

# Gerekli versiyonlar belirtilerek yükleme
uv pip install "numpy>=1.20" "pandas>=1.3"

# Requirements dosyasından yükleme
uv pip install -r requirements.txt
```

### 3. Python REPL Başlat

```bash
# İnteraktif Python konsolu (uvx komutuyla)
uvx python3 -i

# Örnek: İçeri REPL'de komutlar
>>> from levhi_mahfuz import LevhiMahfuzConstants as LMC
>>> print(LMC.BASE_SYSTEM)
11
>>> print(LMC.SIRIUS_FREQUENCY_IHLAL)
1330.99803
```

### 4. Birden Fazla Scriptlerini Zincirle

```bash
# Her script sonrasında sonraki başla
uv run test_11_dimensional_constants.py && uv run simulasyon_11.py

# Başarısızlık sonra durdur
uv run verify_constants.py || echo "Verification failed"
```

---

## 📋 S-M-LASYON_11 İçin Önerilen İş Akışı

### İlk Çalıştırma Sırası:

```bash
# 1️⃣  Sabitlikleri doğrula
uv run verify_constants.py

# 2️⃣  Test çıktılarını kontrol et (96.3% geçme oranı beklenir)
uv run test_11_dimensional_constants.py

# 3️⃣  Monte Carlo simülasyonları çalıştır (100k iterasyon)
uv run uv_monte_carlo_runner.py

# 4️⃣  Ana simülasyon başlat (results.txt'ye yazma yapacak)
uv run simulasyon_11.py

# 5️⃣  İşlenen keşifleri işle
uv run process_discoveries.py

# 6️⃣  Antigravity bridgesi doğrulama (dış kaynaklardan veri oku)
uv run antigravity_bridge.py
```

---

## 🎯 Özel Komut Örnekleri

### KAR TOPU V5 Analiz Çalıştırması

```bash
# Monte Carlo doğrulamalarla KAR TOPU V5 verilerini test et
uv run uv_monte_carlo_runner.py

# Çıktı şu şekilde başlayacak:
# 🌌 11-DIMENSIONAL UNIVERSE - UV MONTE CARLO RUNNER
# 🌟 SIRIUS FREKANS - MONTE CARLO DOĞRULAMA
# 🔒 ENOCH 11D DIMENSION LOCK - MONTE CARLO TEST
# 🔺 GIZA INTEGRAL - MONTE CARLO VALIDATION
# ⚛️  ANTI-GRAVITY MASTER FORMULA - MONTE CARLO TEST
# 📊 MONTE CARLO SIMULATION SUMMARY REPORT
```

### Dashboard Başlat (Flask)

```bash
# Web arayüzünü localhost:5000'de başlat
uv run dashboard_11.py

# Başka bir terminalde test et
curl http://localhost:5000/
```

### Jupyter Notebook Çalışması (Eğer gerekirse)

```bash
# COLAB_MEGA_ANALYSIS.ipynb'i çalıştır
jupyter notebook COLAB_MEGA_ANALYSIS.ipynb
```

---

## 🔧 Ortam Değişkenleri

Eğer özel ortam değişkenleri gerekirse:

```bash
# Export ederek ayarla
export SIMULATIONS_PATH="/workspaces/S-M-LASYON_11"
export LOG_LEVEL="DEBUG"

# Sonra UV komutlarını çalıştır
uv run simulasyon_11.py
```

---

## 📊 Performans İpuçları

### Hızlı Çalıştırma

```bash
# Python'u optimize ederek çalıştır
PYTHONOPTIMIZE=2 uv run simulasyon_11.py

# Multiple simulations paralel (bash)
for i in {1..5}; do
  uv run uv_monte_carlo_runner.py &
done
wait
```

### Profil ve Hata Ayıklama

```bash
# Python profiler ile performans analizi
uv run -m cProfile -s cumulative simulasyon_11.py

# Detaylı hata izlemesi
PYTHONDONTWRITEBYTECODE=1 uv run -u simulasyon_11.py
```

---

## 🐛 Sorun Giderme

### UV çalışmıyor?

```bash
# İlk: PATH'ı yenile
hash -r

# Veya açık yolu kullan
/home/codespace/.local/bin/uv --version

# Yeniden yükle (gerekirse)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### İmport hatası?

```bash
# Tüm bağımlılıkları yeniden yükle
uv pip install -r requirements.txt --force-reinstall

# Veya manuel olarak ekle
uv pip install levhi_mahfuz simulasyon_11
```

### Python versiyon sorunu?

```bash
# Mevcut Python'u kontrol et
python3 --version

# Belirli Python versiyonu taşı
uv run --python 3.12 simulasyon_11.py
```

---

## 📚 Daha Fazla Bilgi

- **Resmi Docs**: https://docs.astral.sh/uv/
- **GitHub**: https://github.com/astral-sh/uv
- **Quick Demo**: `uv --help`

---

## ✨ Başarılı Çalıştırma İşareti

Komut başarıyla çalışırsa:
- ✅ Hiçbir ImportError hatası yok
- ✅ Script sonunda `results.txt` güncellenmiş
- ✅ Ayarlar konsola yazdırıldı (renkli output)
- ✅ Çıkış kodu 0 (başarı)

**Örnek başarılı output:**
```
🌌 11-DIMENSIONAL UNIVERSE - UV MONTE CARLO RUNNER
✓ SIRIUS ALIGNMENT CONFIRMED
✓ ENOCH 11D LOCK VERIFIED
✓ GIZA INTEGRAL VERIFIED
✓ ANTI-GRAVITY FORMULA VALIDATED
✅ SIMULATIONS HIGHLY VALIDATED - SYSTEM OPERATIONAL
```

---

🎉 **Hazır! Artık UV ile tüm scriptleri çalıştırabilirsiniz!**
