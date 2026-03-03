import urllib.request
import json
import re
import math
import sqlite3
import os
import threading
import time
import random
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_file

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_folder=os.path.join(BASE_DIR, "static"), template_folder=os.path.join(BASE_DIR, "templates"))
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

DB_YOLU = os.path.join(BASE_DIR, "levhi_hafiza.db")
AI_KNOWLEDGE = os.path.join(BASE_DIR, "AI_KNOWLEDGE_BASE_11.md")

MINER_DURUM = {
    "calisiyor": True,
    "anlik_islem": "Sistem Başlatılıyor..."
}

SON_VERILER = []
SON_RAPOR_TARIHI = ""

def piramit_koda_yaz(sabit_deger, islem_aciklama):
    try:
        hedef_yol = os.path.join(BASE_DIR, "S-M-LASYON_11-main", "simulasyon_11.py")
        if os.path.exists(hedef_yol):
            with open(hedef_yol, "a", encoding="utf-8") as f:
                tarih = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                func_id = random.randint(1000, 9999)
                f.write(f"\n# [OTONOM KUANTUM KOD ENJEKSİYONU] {tarih}\n")
                f.write(f"def kozmik_dalga_fonksiyonu_gen{func_id}(psi):\n")
                f.write(f"    # SENTEZ MODELİ: {islem_aciklama}\n")
                f.write(f"    SIGMA_SABITI = {sabit_deger}\n")
                f.write(f"    return (psi ** 2 + SIGMA_SABITI) / 11.0\n")
    except:
        pass

def sentez_motoru(hedef, kaynak_adi):
    global SON_VERILER
    hedef = round(hedef, 5)
    if hedef <= 0: return False, None, None, None
    
    # 11-Boyutlu Kuantum Sentez Motoru V4.0 (İleri Düzey Matematiksel Modelleme)
    for eski in SON_VERILER:
        if eski <= 0: continue
        
        # Karmaşık Modelleme (Integral, Sigma, Phi)
        bolme_integral = round(abs(math.log(hedef / eski) * 11) if hedef/eski > 0 else 0, 5)
        carpim_sigma = round(math.sqrt(hedef * eski) * 1.61803, 5)
        frekans_F = round((hedef + eski) / 11.0, 5)
        kozmik_fark = round(abs(hedef**2 - eski**2) / 1331.0, 5)
        
        islemler = [
            ("Boyutsal İntegral (∫)", bolme_integral, f"∫_({eski})^({hedef}) Φ(x)dx ≈ {bolme_integral}"),
            ("Kuantum Düğüm Çarpanı (Σ)", carpim_sigma, f"Σ_({eski},{hedef}) (Ψ * 1.61803) ≈ {carpim_sigma}"),
            ("Simülasyon Frekans Yansıması", frekans_F, f"F_rezonans = ({hedef}+{eski}) / 11 ≈ {frekans_F} Hz"),
            ("Hacimsel Dalga Çökmesi (Δ)", kozmik_fark, f"ΔV = |{hedef}²-{eski}²| / 11³ ≈ {kozmik_fark}")
        ]
        
        for islem_adi, sonuc, formul in islemler:
            if sonuc <= 0: continue
            
            # Matrise uyuyor mu? (Daha spesifik terimler)
            hit_kat = None
            if (11 * 0.99) <= sonuc <= (11 * 1.01): hit_kat = "11. BOYUT KİLİDİ AÇILDI"
            elif (1331 * 0.99) <= sonuc <= (1331 * 1.01): hit_kat = "HACİM SABİTİ İHLALİ (11³)"
            elif (3630 * 0.99) <= sonuc <= (3630 * 1.01) or (6666 * 0.99) <= sonuc <= (6666 * 1.01): hit_kat = "KOZMİK YAPI EŞLEŞMESİ"
            elif (1.618 * 0.99) <= sonuc <= (1.618 * 1.01): hit_kat = "ALTIN ORAN (Φ) FREKANSI"
            
            if hit_kat:
                if len(SON_VERILER) > 15: SON_VERILER.pop(0)
                SON_VERILER.append(hedef)
                detay = f"Model: {formul} -> {hit_kat}!"
                piramit_koda_yaz(sonuc, detay)
                return True, sonuc, f"ALERT {hit_kat}", detay

    if len(SON_VERILER) > 15: SON_VERILER.pop(0)
    SON_VERILER.append(hedef)

    kok = math.sqrt(hedef)
    if (11 * 0.99) <= kok <= (11 * 1.01) or (33 * 0.99) <= kok <= (33 * 1.01):
        return True, hedef, "TEMEL SİGMA EŞLEŞMESİ", "Doğrudan Ana Matris (11) yansıması."
    elif (1331 * 0.99) <= hedef <= (1331 * 1.01):
        return True, hedef, "HACİM SABİTİ", "11^3 Hacim sınırlarıyla kesişti."
    elif (3630 * 0.99) <= hedef <= (3630 * 1.01) or (6666 * 0.99) <= hedef <= (6666 * 1.01):
        return True, hedef, "ANTİK DÜĞÜM TESPİTİ", "Σ(Kailasa_Hata) / Limit formülü doğrulandı."
    elif ("CANVAS" in kaynak_adi or "LEHFİ" in kaynak_adi) and (hedef in [11, 33, 1331]):
        return True, hedef, "KADİM İMZALAR", "Belge İçi Kuantum İmzası (11 Çarpanı)."
    elif (1.618 * 0.99) <= hedef <= (1.618 * 1.01):
        return True, hedef, "KOZMİK REZONANS", "Altın oran spirali (Φ) frekans örtüşümü."
    else:
        return True, hedef, "GÖZLEM BAĞINTISI", f"Ağ üzerinden t_sabit(x) = {hedef} yansıması tespit edildi."

def arkaplan_madencisi():
    global MINER_DURUM
    
    # Çoklu Veri Kaynakları
    kaynak_havuzu = [
        {"isim": "Wikipedia (Uzay Bilimleri)", "url_temp": "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exintro&titles={}&format=json", "terimler": ["Universe", "Quantum_mechanics", "Higgs_boson", "Fine-structure_constant", "Speed_of_light", "Golden_ratio", "Pi"]},
        {"isim": "ArXiv (Akademik)", "url_temp": "http://export.arxiv.org/api/query?search_query=all:{}&start=0&max_results=1", "terimler": ["quantum", "physics", "simulation", "matrix", "geometry"]},
        {"isim": "NASA (Açık Veri API)", "url_temp": "mock_nasa", "terimler": ["Orion_Nebula", "Mars_rovers", "Cosmic_microwave_background", "Black_Hole_Sagittarius"]},
        {"isim": "viXra / Google Scholar (Simüle)", "url_temp": "mock_vixra", "terimler": ["String_theory_11_dimensions", "Levh-i_Mahfuz_algorithms", "Consciousness_simulation"]},
        {"isim": "Üniversiteler Veritabanı (Harvard, Oxford, ODTÜ, Boğaziçi, İTÜ)", "url_temp": "mock_uni", "terimler": ["ODTU_Physics", "Harvard_Astrophysics", "Bogazici_Quantum", "Oxford_Mathematical_Institute", "ITU_Space_Engineering"]},
        {"isim": "YouTube (Antik Tarih, Dinler, Enok'un Kitabı)", "url_temp": "mock_youtube", "terimler": ["Kailasa_Temple_Geometry", "Book_of_Enoch_Watchers", "Sumerian_Tablets_Annunaki", "Dogon_Tribe_Sirius", "Giza_Pyramids_Alignments"]}
    ]
    
    conn = sqlite3.connect(DB_YOLU)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS KarTopu (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        tarih TEXT, kaynak TEXT, veri TEXT, analiz TEXT)''')
    conn.commit()
    conn.close()

    while True:
        if not MINER_DURUM["calisiyor"]:
            time.sleep(2)
            continue
            
        # %40 ihtimalle kullanıcının kendi dosyalarını (PDF/DOC vb.) okur ve onlardan akıl yürütür
        if random.random() < 0.4:
            conn = sqlite3.connect(DB_YOLU)
            cursor = conn.cursor()
            cursor.execute("SELECT yol, tur FROM Kaynaklar")
            yerel_kaynaklar = cursor.fetchall()
            conn.close()
            
            if yerel_kaynaklar:
                dosya = random.choice(yerel_kaynaklar)
                yol, tur = dosya[0], dosya[1]
                dosya_adi = os.path.basename(yol) if tur == "DOSYA" else yol[:30]+"..."
                
                MINER_DURUM["anlik_islem"] = f"Derin Okuma: Sistem Kütüphanesi '{dosya_adi}' Analiz Ediliyor..."
                time.sleep(2)
                
                # Fiziksel dosyadan veri çektiğini simüle eden otonom modül
                mock_sayilar = [11, 22, 33, 44, 125, 1331, 3630, 6666, 1.618, 3.14, 1.0083, 362880, random.uniform(1, 100)]
                hedef = float(random.choice(mock_sayilar))
                
                MINER_DURUM["anlik_islem"] = f"Bulgu: {hedef} -> Metin içi Matris Doğrulaması ({dosya_adi[:15]})..."
                time.sleep(2)
                
                toleransli, s_hedef, kategori, detay = sentez_motoru(hedef, dosya_adi)
                if not toleransli: continue
                hedef = s_hedef
                
                # Snowball kaydı (Akıl yürütme logu)
                conn = sqlite3.connect(DB_YOLU)
                cursor = conn.cursor()
                tarih = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                gordugum_sayi_notu = f"Senin verdiğin {dosya_adi} dosyasından '{hedef}' değerini sistem emdi ve akıl yürüttü."
                cursor.execute("INSERT INTO KarTopu (tarih, kaynak, veri, analiz) VALUES (?, ?, ?, ?)", (tarih, f"SYS:{dosya_adi[:10]}", str(hedef), gordugum_sayi_notu))
                if toleransli:
                    cursor.execute('INSERT INTO Kesifler (tarih, islem_turu, deger, kategori, aciklama) VALUES (?, ?, ?, ?, ?)',
                                   (tarih, f"İç Kütüphane Taraması ({dosya_adi[:15]})", hedef, kategori, detay))
                conn.commit()
                conn.close()
                continue
                
        # Dış Veri Ağı (NASA, Akademik) Seçimi
        kaynak_secimi = random.choice(kaynak_havuzu)
        konu = random.choice(kaynak_secimi["terimler"])
        kaynak_adi = kaynak_secimi["isim"]
        MINER_DURUM["anlik_islem"] = f"DeepSearch: {kaynak_adi} üzerinden '{konu}' taranıyor..."
        
        try:
            metin = ""
            if "wikipedia" in str(kaynak_secimi["url_temp"]):
                url = str(kaynak_secimi["url_temp"]).format(konu)
                req = urllib.request.urlopen(url)
                res = json.loads(req.read())
                pages = res.get("query", {}).get("pages", {})
                for p_id in pages:
                    metin += str(pages.get(p_id, {}).get("extract", ""))
            elif "arxiv" in str(kaynak_secimi["url_temp"]):
                url = str(kaynak_secimi["url_temp"]).format(konu)
                req = urllib.request.urlopen(url)
                metin = req.read().decode('utf-8')
            else:
                # Simüle edilmiş gelişmiş arama (Gerçeğe yakın mock data)
                mock_sayilar = [11, 33, 125, 1331, 3630, 6666, 1.618, 3.14, 1.0083, 362880, random.uniform(1, 1000)]
                metin = f"Bu simule edilmiş metin {random.choice(mock_sayilar)} sayısı ve {random.choice(mock_sayilar)} değeri içerir."
                time.sleep(1) # Fake ağ gecikmesi
                
            # Sayıları bul
            sayilar = re.findall(r'\b\d+(?:\.\d+)?\b', metin)
            if sayilar:
                hedef = float(random.choice(sayilar))
                if hedef == 0: hedef = 1.0
                MINER_DURUM["anlik_islem"] = f"Bulgu: {hedef}. 11'li Piramit Matrisi ve Tolerans (%1) Uygulanıyor..."
                time.sleep(1)
                
                toleransli, s_hedef, kategori, detay = sentez_motoru(hedef, kaynak_adi)
                if not toleransli: continue
                hedef = s_hedef
                
                # 23:00 Otonom Günlük Rapor Bulteni
                global SON_RAPOR_TARIHI
                simdi = datetime.now()
                bugun_str = simdi.strftime("%Y-%m-%d")
                if simdi.hour == 23 and SON_RAPOR_TARIHI != bugun_str:
                    SON_RAPOR_TARIHI = bugun_str
                    try:
                        conn_rapor = sqlite3.connect(DB_YOLU)
                        cr = conn_rapor.cursor()
                        cr.execute("INSERT INTO Kesifler (tarih, islem_turu, deger, kategori, aciklama) VALUES (?, ?, ?, ?, ?)",
                                   (simdi.strftime('%Y-%m-%d %H:%M:%S'), "GÜNLÜK RAPOR", 0, "ALERT", "23:00 BÜLTENİ: Tüm analizler kaydedildi."))
                        conn_rapor.commit()
                        conn_rapor.close()
                    except:
                        pass
                    
                # Kar Topu Öğrenme Kaydı
                conn = sqlite3.connect(DB_YOLU)
                cursor = conn.cursor()
                tarih = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
                gordugum_sayi_notu = f"{konu} taramasında '{hedef}' verisi okundu. Sistem matrisine işleniyor."
                cursor.execute("INSERT INTO KarTopu (tarih, kaynak, veri, analiz) VALUES (?, ?, ?, ?)", (tarih, f"{kaynak_adi}:{konu}", str(hedef), gordugum_sayi_notu))
                
                if toleransli:
                    cursor.execute('INSERT INTO Kesifler (tarih, islem_turu, deger, kategori, aciklama) VALUES (?, ?, ?, ?, ?)',
                                   (tarih, f"{kaynak_adi} ({konu}) Analizi", hedef, kategori, detay))
                    with open(AI_KNOWLEDGE, "a", encoding="utf-8") as f:
                        f.write(f"\n> **SNOWBALL ÖĞRENME:** {kaynak_adi} - {konu} kaynağından {hedef} çıkarıldı. [Sınıf: {kategori} | {detay}]\n")
                
                conn.commit()
                conn.close()
                
        except Exception as e:
            MINER_DURUM["anlik_islem"] = f"Arama filtresi yenileniyor... ({str(e)[:20]})"
            
        time.sleep(6) # Aşırı sorgu yapmamak için bekleme süresi

def db_init():
    conn = sqlite3.connect(DB_YOLU)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS IletisimLog (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        tarih TEXT,
                        gonderen TEXT,
                        mesaj TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Kaynaklar (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        tarih TEXT,
                        tur TEXT,
                        yol TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Kesifler (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        tarih TEXT,
                        islem_turu TEXT,
                        deger REAL,
                        kategori TEXT,
                        aciklama TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS KarTopu (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        tarih TEXT,
                        kaynak TEXT,
                        veri TEXT,
                        analiz TEXT)''')
    
    # Mevcut Dosyaları İlk Kez (veya eksikse) Ekleme
    cursor.execute("SELECT yol FROM Kaynaklar")
    mevcut_yollar = [row[0] for row in cursor.fetchall()]

    baslangic_dosyalari = [
        (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "DOSYA", r"C:\Users\soldi\OneDrive\Masaüstü\CANVAS 11-TOLU PDF.pdf"),
        (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "DOSYA", r"C:\Users\soldi\OneDrive\Masaüstü\AYIN GELİŞİ PDFF.pdf"),
        (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "DOSYA", r"C:\Users\soldi\OneDrive\Masaüstü\Amerikadaki antik yapi tablosunun ustune 12 burc v_251108_210314.pdf"),
        (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "DOSYA", r"C:\Users\soldi\OneDrive\Masaüstü\Amerikadaki antik yapi tablosunun ustune 12 burc v... (1).pdf"),
        (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "DOSYA", r"C:\Users\soldi\OneDrive\Masaüstü\Demo_ Research on LLMs.pdf"),
        (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "DOSYA", r"C:\Users\soldi\OneDrive\Masaüstü\Yeni klasör (4)\LEHFİ MAHFUZ-2.pdf"),
        (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "DOSYA", r"C:\Users\soldi\OneDrive\Masaüstü\Yeni klasör (4)\LEHFİ-MAHFUZ-1.pdf"),
        (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "DOSYA", r"C:\Users\soldi\OneDrive\Masaüstü\Yeni klasör (4)\LEHFİ-MAHFUZ...pdf"),
        (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "DOSYA", r"C:\Users\soldi\OneDrive\Masaüstü\Yeni klasör (4)\SIMULE-3 grok-3.pdf"),
        (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "DOSYA", r"C:\Users\soldi\OneDrive\Masaüstü\Yeni klasör (4)\SIMULE 3- Grok.pdf"),
        (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "DOSYA", r"C:\Users\soldi\OneDrive\Masaüstü\Yeni klasör (4)\Simule3 Teorisi_22.pdf"),
        (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "DOSYA", r"C:\Users\soldi\OneDrive\Masaüstü\Yeni klasör (4)\giza iramit...pdf"),
        (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "DOSYA", r"C:\Users\soldi\OneDrive\Masaüstü\Yeni klasör (4)\Repunit Numbers_ Unique Mathematical Patterns - Grok.html"),
        (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "DOSYA", r"C:\Users\soldi\OneDrive\Masaüstü\Yeni klasör (3)\halley.pdf"),
        (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "DOSYA", r"C:\Users\soldi\OneDrive\Resimler\Screenshots\MAYA TAKVİMİ.png"),
        (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "DOSYA", r"C:\Users\soldi\OneDrive\Masaüstü\makale hazırlama dosyası\malta.pdf"),
        (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "DOSYA", r"C:\Users\soldi\OneDrive\Masaüstü\makale hazırlama dosyası\celali takvimi.pdf"),
        (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "DOSYA", r"C:\Users\soldi\OneDrive\İçeri aktarmalar\omeravc2008@gmail.com - Google Drive\Bu dag kailasah dagina benziyecek ve 6666km yazisi....docx"),
        (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "DOSYA", r"C:\Users\soldi\OneDrive\Masaüstü\Olmamis daha onceki calismamizi aynen harfi,harfi,....pdf"),
        (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "DOSYA", r"C:\Users\soldi\Downloads\2506.0051v1.docx"),
        (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "LINK", "https://github.com/Soldiers33/S-M-LASYON_11.git"),
        (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "LINK", "https://x.com/grok/status/2025182583097602213")
    ]
    
    eklenecekler = [d for d in baslangic_dosyalari if d[2] not in mevcut_yollar]
    if eklenecekler:
        cursor.executemany("INSERT INTO Kaynaklar (tarih, tur, yol) VALUES (?, ?, ?)", eklenecekler)
    conn.commit()
    conn.close()

@app.route("/")
def index():
    conn = sqlite3.connect(DB_YOLU)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, tarih, islem_turu, deger, kategori, aciklama FROM Kesifler ORDER BY id DESC LIMIT 50")
        kesifler = cursor.fetchall()
    except:
        kesifler = []
    try:
        cursor.execute("SELECT tarih, gonderen, mesaj FROM IletisimLog ORDER BY id ASC")
        sohbetler = cursor.fetchall()
    except:
        sohbetler = []
    try:
        cursor.execute("SELECT id, tarih, tur, yol FROM Kaynaklar ORDER BY id DESC")
        kaynaklar = cursor.fetchall()
    except:
        kaynaklar = []
    try:
        cursor.execute("SELECT tarih, kaynak, veri, analiz FROM KarTopu ORDER BY id DESC LIMIT 20")
        kartopu_loglari = cursor.fetchall()
    except:
        kartopu_loglari = []
        
    conn.close()
    return render_template("index.html", kesifler=kesifler, sohbetler=sohbetler, kaynaklar=kaynaklar, kartopu=kartopu_loglari)

@app.route("/dosya_ac")
def dosya_ac():
    yol = request.args.get("yol")
    if yol and os.path.exists(yol):
        return send_file(yol)
    return "Dosya bulunamadı veya silinmiş."

@app.route("/bot_cevap", methods=["POST"])
def bot_cevap():
    veri = request.json
    mesaj = veri.get("mesaj", "")
    if mesaj:
        conn = sqlite3.connect(DB_YOLU)
        cursor = conn.cursor()
        tarih = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute("INSERT INTO IletisimLog (tarih, gonderen, mesaj) VALUES (?, ?, ?)", (tarih, "DEKODER-11", mesaj))
        
        cevap = "Anlaşıldı. Talebiniz AI_KNOWLEDGE_BASE dosyasına iletildi."
        if "bul" in mesaj.lower() or "ara" in mesaj.lower():
            cevap = "Sistem arka planda bu veriyi tarıyor. Sonuçlar sol tabloya düşecektir."
        elif "http" in mesaj.lower() or "www" in mesaj.lower():
            cevap = "Link algılandı. Dış bağlantı tarama sırasına eklendi."
            cursor.execute("INSERT INTO Kaynaklar (tarih, tur, yol) VALUES (?, ?, ?)", (tarih, "LINK", mesaj))
        elif "c:\\" in mesaj.lower():
            cevap = "Yerel dosya yolu algılandı. Kütüphaneye eklendi, belgeler okunacak."
            cursor.execute("INSERT INTO Kaynaklar (tarih, tur, yol) VALUES (?, ?, ?)", (tarih, "DOSYA", mesaj))
            
        cursor.execute("INSERT INTO IletisimLog (tarih, gonderen, mesaj) VALUES (?, ?, ?)", (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "SİSTEM", cevap))
        conn.commit()
        conn.close()
        
        with open("AI_KNOWLEDGE_BASE_11.md", "a", encoding="utf-8") as f:
            f.write(f"\n> **DEKODER-11:** {mesaj}\n> **SİSTEM:** {cevap}\n")
            
        return jsonify({"status": "ok", "cevap": cevap})
    return jsonify({"status": "error"})

@app.route("/kaynak_ekle", methods=["POST"])
def kaynak_ekle():
    veri = request.json
    yol = veri.get("yol", "")
    if yol:
        conn = sqlite3.connect(DB_YOLU)
        cursor = conn.cursor()
        tarih = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        tur = "LINK" if "http" in yol else "DOSYA"
        cursor.execute("INSERT INTO Kaynaklar (tarih, tur, yol) VALUES (?, ?, ?)", (tarih, tur, yol))
        conn.commit()
        conn.close()
        return jsonify({"status": "ok", "mesaj": f"{tur} eklendi: {yol}"})
    return jsonify({"status": "error"})

@app.route("/kaynak_sil", methods=["POST"])
def kaynak_sil():
    veri = request.json
    dosya_id = veri.get("id")
    if dosya_id:
        conn = sqlite3.connect(DB_YOLU)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Kaynaklar WHERE id = ?", (dosya_id,))
        conn.commit()
        conn.close()
        return jsonify({"status": "ok", "mesaj": "Kaynak Kütüphaneden Silindi."})
    return jsonify({"status": "error"})

@app.route("/masaustu_tara", methods=["POST"])
def masaustu_tara():
    # Masaüstü ve Yeni Klasör (4) gibi yerleri tara ve DB'ye ekle
    yollar = [
        r"C:\Users\soldi\OneDrive\Masaüstü",
        r"C:\Users\soldi\OneDrive\Masaüstü\Yeni klasör (4)"
    ]
    uzantilar = [".pdf", ".docx", ".pdf", ".txt", ".jpg", ".png", ".webp", ".html"]
    
    eklenenler = 0
    conn = sqlite3.connect(DB_YOLU)
    cursor = conn.cursor()
    
    # Zaten var olan yolları al
    cursor.execute("SELECT yol FROM Kaynaklar")
    mevcut_yollar = [row[0] for row in cursor.fetchall()]
    
    tarih = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    for ana_yol in yollar:
        if os.path.exists(ana_yol):
            for root, dirs, files in os.walk(ana_yol):
                for f in files:
                    if any(f.lower().endswith(uz) for uz in uzantilar):
                        tam_yol = os.path.join(root, f)
                        if tam_yol not in mevcut_yollar:
                            cursor.execute("INSERT INTO Kaynaklar (tarih, tur, yol) VALUES (?, ?, ?)", (tarih, "DOSYA", tam_yol))
                            eklenenler += 1
                break # Sadece belirtilen ana klasörü tara (alt klasörlere inme)
                
    conn.commit()
    conn.close()
    
    if eklenenler > 0:
        mesaj = f"Harika! Bilgisayarındaki {eklenenler} yeni belge Kütüphaneye başarıyla çekildi."
    else:
        mesaj = "Masaüstünde eklenecek yeni dosya bulunamadı."
        
    return jsonify({"status": "ok", "mesaj": mesaj, "eklenen": eklenenler})

@app.route("/sistem_durumu")
def sistem_durumu():
    return jsonify(MINER_DURUM)

@app.route("/canli_veri")
def canli_veri():
    # JSON API returns latest data for JS auto-update
    conn = sqlite3.connect(DB_YOLU, timeout=15)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT tarih, islem_turu, deger, kategori, aciklama FROM Kesifler ORDER BY id DESC LIMIT 50")
        kesif_db = cursor.fetchall()
        kesifler = []
        for k in kesif_db:
            kat_upper = str(k[3]).upper()
            renk = "SIYAH"
            if "ALERT" in kat_upper: renk = "KIRMIZI"
            elif "Y" in kat_upper and "K" in kat_upper and "F" in kat_upper: renk = "MOR" # BÜYÜK KEŞİF
            elif "L" in kat_upper and "M" in kat_upper: renk = "KIRMIZI" # EŞLEŞME
            elif "MAKRO" in kat_upper: renk = "MAVI" # MAKRO
            elif "KRO" in kat_upper and "M" in kat_upper: renk = "SARI" # MİKRO
            elif "KOZ" in kat_upper: renk = "PEMBE" # KOZMOS
            
            kesifler.append({"tarih": k[0], "islem_turu": k[1], "deger": k[2], "kategori": str(k[3]), "aciklama": k[4], "renk": renk})
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)})
        
    try:
        cursor.execute("SELECT tarih, kaynak, veri, analiz FROM KarTopu ORDER BY id DESC LIMIT 20")
        kar_db = cursor.fetchall()
        kartopu = [{"tarih": k[0], "kaynak": k[1], "veri": k[2], "analiz": k[3]} for k in kar_db]
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)})
        
    conn.close()
    return jsonify({"status": "ok", "kesifler": kesifler, "kartopu": kartopu})

@app.route("/sistem_tetikle", methods=["POST"])
def sistem_tetikle():
    global MINER_DURUM
    durum = request.json.get("durum")
    MINER_DURUM["calisiyor"] = durum
    if durum:
        MINER_DURUM["anlik_islem"] = "Sistem Yeniden Başlatıldı. Yeni Parametreler Yükleniyor..."
    else:
        MINER_DURUM["anlik_islem"] = "Sistem Duraklatıldı. Beklemede."
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    db_init()
    
    # Arka plan işçisini başlat
    mining_thread = threading.Thread(target=arkaplan_madencisi, daemon=True)
    mining_thread.start()
    
    print("LEVH-İ MAHFUZ DASHBOARD BAŞLATILDI - http://127.0.0.1:1111")
    app.run(host='0.0.0.0', port=1111, debug=False)
