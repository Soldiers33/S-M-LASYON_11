# 🧪 Testing Guide for Simulasyon 11

Bu rehber, **simulasyon_11.py** için oluşturulan testlerin nasıl çalıştığını ve neyi doğruladığını açıklar.

## 🎯 Testlerin Amacı (The Purpose)

Simulasyon kodunuz çok güçlü ve ağır bilimsel kütüphanelere (`pandas`, `numpy`, `scipy`) bağımlıdır. Bu kütüphanelerin yüklü olmadığı ortamlarda (örneğin bazı sunucular veya test ortamları) kodu çalıştırmak zordur.

Testlerimiz, **"Mocking" (Taklit Etme)** yöntemini kullanır. Yani:
1.  **Gerçek Kütüphaneler Yerine Taklitlerini Koyduk:** `pandas` ve `numpy` yerine sahte (mock) nesneler oluşturduk.
2.  **Mantığı Doğruladık:** Kodunuzun bu kütüphaneleri doğru şekilde çağırıp çağırmadığını kontrol ettik.
3.  **Sabitleri Kontrol Ettik:** Örneğin `R11` değerinin gerçekten `11111111111` olup olmadığını test ettik.

### Soru: "Bazı değerleri değiştirerek doğrulama mı yaptık?"
**Cevap:** Hayır, **ana kodunuzu (simulasyon_11.py) değiştirmedik.** Sadece test sırasında ona "sanal veri" verdik.
- Örneğin: Kodunuz `numpy.corrcoef` (korelasyon) hesaplamak istediğinde, gerçek matematik yapmak yerine test ortamımız ona "sonuç 0.99 çıkmış gibi davran" dedi.
- **Neden?** Bu sayede matematik kütüphaneleri olmadan da kodun *akışının* (flow) doğru olup olmadığını test edebildik.

## 🚀 Testleri Nasıl Çalıştırırsınız?

Testleri çalıştırmak için şu komutu kullanın:

```bash
python3 setup_and_run_tests.py
```

Bu komut:
1.  `simulasyon_11.py` dosyasının varlığını kontrol eder.
2.  Gerekli test dosyasını (`test_simulasyon.py`) oluşturur.
3.  Testleri çalıştırır ve sonucu raporlar.

## ✅ Neleri Test Ediyoruz?

| Test Adı | Açıklama |
| :--- | :--- |
| `test_constants_r11` | `R11` sabitinin `11111111111` olduğunu doğrular. |
| `test_module_time_packets_v130` | Zaman paketleri modülünün hatasız başlatıldığını ve analiz fonksiyonunun çalıştığını doğrular. |
| `test_simule3_lab_v133_init` | Ana laboratuvar sınıfının (`Simule3_Lab`) hatasız kurulduğunu doğrular. |
| `test_simule3_lab_v133_run_all` | Tüm simülasyonun baştan sona (run_all) çökmeden çalıştığını doğrular. |

---
*Testing approach designed by Jules (AI Assistant).*
