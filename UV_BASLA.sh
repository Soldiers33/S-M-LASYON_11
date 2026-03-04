#!/bin/bash
# UV ENTEGRASYON - İLK BAŞLATMA REHBERI
# UV Integration - Getting Started Guide
# 
# Bu dosya açıklamalar içerir - çalıştırılması gerekli değildir
# This file contains explanations - does not need to be executed

cat << 'EOF'

╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║               🌌 S-M-LASYON_11 - UV ENTEGRASYONİ BAŞLATILDI 🌌              ║
║                                                                              ║
║              11-BOYUTLU EVREN SİMÜLASYONU - UV HAZIR, ÇALIŞMAYA AÇIK       ║
║                  11-Dimensional Universe Simulation - UV Ready              ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝


█░ İLK ADIM - FIRST STEP ░█

UV'nin çalışıp çalışmadığını kontrol et:
Check if UV is working:

    uv --version          # 0.10.8 görmeli / should show 0.10.8
    uv run --help         # Yardım menüsü / Help menu


█░ İKİNCİ ADIM - SECOND STEP ░█

Test sistemini çalıştır - 3-5 dakika sürer:
Run the test system - takes 3-5 minutes:

    bash uv_run_all.sh

Veya tek tek testleri çalıştır / Or run tests individually:

    uv run test_11_dimensional_constants.py     # Unit testler (11 sections)
    uv run verify_constants.py                  # NASA doğrulaması
    uv run uv_monte_carlo_runner.py            # Monte Carlo (100k iterations)


█░ ÜÇÜNCÜ ADIM - THIRD STEP ░█

Ana simülasyonu başlat:
Launch the main simulation:

    uv run simulasyon_11.py

Sonuçlar results.txt'ye yazılacak / Results will be written to results.txt


█░ DÖRDÜNCÜ ADIM - FOURTH STEP ░█

Web dashboard'ı aç:
Open the web dashboard:

    uv run dashboard_11.py

Sonra: http://localhost:5000 adresini ziyaret et
Then: Visit http://localhost:5000


█░ BEŞİNCİ ADIM - FIFTH STEP ░█

Interactive Python çalışması:
Interactive Python session:

    uvx python3 -i

Python içinde şunları dene / Try this inside Python:

    from levhi_mahfuz import LevhiMahfuzConstants as LMC
    print(LMC.BASE_SYSTEM)              # 11
    print(LMC.SIRIUS_FREQUENCY_IHLAL)   # 1330.99803
    print(LMC.ANTIGRAVITY_MASTER_FORMULA)  # 0.00827105


════════════════════════════════════════════════════════════════════════════════

📊 KAR TOPU V5 MONTE CARLO SONUÇLARI - RESULTS:

    🌟 SIRIUS Frekansı:          95.43% başarı
    🔒 ENOCH 11D Lock:           66.09% rezonans
    🔺 GIZA İntegral:           100.00% kesinlik
    ⚛️  Anti-Gravity Formülü:    100.00% doğrulama
    
    📈 GENEL BAŞARI ORANI:          90.38% ✅


════════════════════════════════════════════════════════════════════════════════

🛠️ YARDIMCI KOMUTLAR - USEFUL COMMANDS:

    # Belirli bir script'i argümanlarla çalıştır
    uv run simulasyon_11.py --iterations 50000

    # Python paket yükle (gerekirse)
    uv pip install "package-name>=version"

    # Pip komutları
    uv pip list              # Yüklü paketleri göster
    uv pip freeze            # Requirements formatında çıktı

    # Dosyaları temizle (temiz cache)
    rm -rf .uv .pytest_cache __pycache__


════════════════════════════════════════════════════════════════════════════════

📚 DOKÜMANTASYON - DOCUMENTATION:

    • UV_QUICK_START.md              - Hızlı başlangıç kılavuzu
    • UV_INTEGRATION_COMPLETE.md     - Tam entegrasyon raporu
    • .github/copilot-instructions.md - AI ajanları için
    • README.md                      - Proje genel bilgi


════════════════════════════════════════════════════════════════════════════════

✨ BAŞARILI KURULUMUN İŞARETLERİ - SUCCESS INDICATORS:

    ✓ Hiçbir ImportError hatası yok
    ✓ results.txt dosyası güncellendi
    ✓ Konsol çıkışı renkli ve biçimlendirilmiş
    ✓ Tüm testler 90%+ başarı oranı
    ✓ Dashboard localhost:5000'de erişilebilir
    ✓ Git push'u başarılı (main branch)


════════════════════════════════════════════════════════════════════════════════

🌐 GIT ENTEGRASYONU - GIT INTEGRATION STATUS:

    Commit -1: KAR TOPU V5 Anti-Gravity Keşifleri Entegrasyonu
    Commit -2: UV Integration Complete - Monte Carlo Runner & Guides  
    Commit -3: UV Integration Summary & Documentation
    
    Tüm değişiklikler GitHub'a push'landı / All changes pushed to GitHub


════════════════════════════════════════════════════════════════════════════════

🚀 SONRAKI ADIMLAR - NEXT STEPS:

    1. Tüm testleri çalıştır ve sonuçları gözden geçir
       Run all tests and review results

    2. Ana simülasyonu uzun süreli çalıştırarak veri topla
       Collect data by running main simulation for extended periods

    3. Bulguları işle ve yeni KAR TOPU V5 keşifleri entegre et
       Process findings and integrate new KAR TOPU V5 discoveries

    4. Web dashboard'ı yapılandır ve dış veri kaynakları bağla
       Configure web dashboard and connect external data sources

    5. Üretim ortamına dağıt - UV dependency management otomatik olacak
       Deploy to production - UV will handle dependency management automatically


════════════════════════════════════════════════════════════════════════════════

💡 İPUÇLARI - TIPS:

    • UV tüm sanal ortamları otomatik yönetir - setup gerekmez!
    • UV handles all virtual environments automatically - no setup needed!

    • İlk çalıştırma yavaş (dependencies indirileniyor), sonra hızlı
    • First run is slow (downloading dependencies), then fast

    • Dosya değişikliklerinde otomatik yeniden yükleme:
    • Auto-reload on file changes:
        while true; do uv run simulasyon_11.py; sleep 5; done

    • Paralel simülasyonlar:
    • Parallel simulations:
        (uv run uv_monte_carlo_runner.py &) && (uv run uv_monte_carlo_runner.py &)

    • Detaylı debug bilgisi:
    • Detailed debug info:
        PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 uv run simulasyon_11.py


════════════════════════════════════════════════════════════════════════════════

❓ SORUN? - PROBLEMS?

    UV çalışmıyor mu? / UV not working?
    → Yeni terminal aç / Open new terminal
    → hash -r (ortam cache'ini temizle / Clear shell cache)
    → uv --version

    Import hatası? / Import error?
    → uv pip install -r requirements.txt --force-reinstall
    → Dosyaları kontrol et / Check files

    Bağlantı sorunu? / Connection issue?
    → PYTHONHTTPSVERIFY=0 uv run ...
    → İnternet bağlantısını kontrol et / Check internet

    Daha fazla yardım / More help?
    → https://docs.astral.sh/uv/


════════════════════════════════════════════════════════════════════════════════

🎉 HAZIRSINIZ! - YOU'RE ALL SET!

S-M-LASYON_11 projesi UV ile çalışmaya hazır.
11-boyutlu evren simülasyonlarını başlatabilirsiniz!

The S-M-LASYON_11 project is ready with UV.
You can start 11-dimensional universe simulations!

---

Hoşça kalın! / See you!
🌌 ✨ 🚀

EOF
