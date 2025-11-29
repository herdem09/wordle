import random # Rastgele seçimler yapmak için 'random' modülünü içe aktarır.
import os # İşletim sistemi fonksiyonlarını (örneğin ekranı temizleme) kullanmak için 'os' modülünü içe aktarır.

KIRMIZI = '\033[91m' # ANSI Kırmızı renk kodunu tanımlar.
SARI = '\033[93m' # ANSI Sarı renk kodunu tanımlar.
YESIL = '\033[92m' # ANSI Yeşil renk kodunu tanımlar.
RESET = '\033[0m' # Rengi sıfırlama kodunu tanımlar.

def tr_upper(metin): # Türkçe karakterleri büyük harfe çeviren fonksiyonu tanımlar.
    TR_UPPER_MAP = { # Türkçe küçük harflerin büyük harf karşılıklarını içeren bir sözlük oluşturur.
        ord('i'): 'İ', ord('ı'): 'I', # 'i' ve 'ı' harfleri için özel eşleşmeler.
        ord('ç'): 'Ç', ord('ğ'): 'Ğ', # Diğer Türkçe karakterler için eşleşmeler.
        ord('ö'): 'Ö', ord('ş'): 'Ş',
        ord('ü'): 'Ü'
    }
    return metin.upper().translate(TR_UPPER_MAP) # Metni önce standart büyük harfe, sonra özel Türkçe harflere çevirir.

def word_chooser(lang, letter_count): # Belirtilen dilde ve uzunlukta rastgele kelime seçen fonksiyonu tanımlar.
    dosya_yolu = f"words/lang/{lang}/length/{letter_count}_letter_words.txt" # Kelime dosyası yolunu oluşturur.
    
    try: # Dosya okuma işlemini hata yakalama bloğu içine alır.
        with open(dosya_yolu, "r", encoding="utf-8") as file: # Dosyayı okuma modunda UTF-8 kodlamasıyla açar.
            lines = file.readlines() # Dosyadaki tüm satırları bir liste olarak okur.
    except FileNotFoundError: # Dosya bulunamazsa hatayı yakalar.
        print(f"Hata: {dosya_yolu} bulunamadı.") # Hata mesajını ekrana yazar.
        return None # Fonksiyondan None değeri ile çıkar.

    if not lines: # Dosya boşsa veya kelime yoksa kontrol eder.
        return None # Fonksiyondan None değeri ile çıkar.
        
    return random.choice(lines).strip() # Satırlardan rastgele birini seçer ve başındaki/sonundaki boşlukları silip döndürür.

def temizle_ekran(): # Konsolu temizleyen fonksiyonu tanımlar.
    os.system('cls' if os.name == 'nt' else 'clear') # İşletim sistemi Windows ise 'cls', değilse 'clear' komutunu çalıştırır.

def dil_sec(): # Kullanıcıdan dil seçimi alan fonksiyonu tanımlar.
    while True: # Geçerli bir seçim yapılana kadar döngüyü sürdürür.
        print("\n" + "=" * 40) # Ayırıcı çizgi yazar.
        print(" DİL SEÇİMİ / LANGUAGE SELECTION") # Başlık yazar.
        print("=" * 40) # Ayırıcı çizgi yazar.
        print("1. Türkçe") # Türkçe seçeneğini gösterir.
        print("2. English") # İngilizce seçeneğini gösterir.
        secim = input("\nSeçiminiz / Your choice (1/2): ").strip() # Kullanıcıdan giriş alır ve boşlukları siler.
        
        if secim == "1": # Seçim 1 ise (Türkçe).
            return "tr" # 'tr' döndürür.
        if secim == "2": # Seçim 2 ise (İngilizce).
            return "en" # 'en' döndürür.
        
        print("Lütfen 1 veya 2 seçin! / Please choose 1 or 2!") # Geçersiz seçim uyarısı verir.

def kelime_yukle(harf_sayisi, dil): # Rastgele bir kelime yükleyen ve büyük harfe çeviren fonksiyonu tanımlar.
    kelime = word_chooser(dil, harf_sayisi) # Kelime seçici fonksiyonu ile rastgele kelimeyi alır.
    if kelime is None: # Kelime bulunamazsa.
        return None # None döndürür.
        
    if dil == "tr": # Dil Türkçe ise.
        return tr_upper(kelime) # tr_upper fonksiyonu ile büyük harfe çevirir.
    return kelime.upper() # Diğer diller için standart upper() metodu ile büyük harfe çevirir.

def hak_sayisi_al(dil): # Kullanıcıdan pozitif bir hak sayısı alan fonksiyonu tanımlar.
    mesaj = "\nKaç hak istersiniz? " if dil == "tr" else "\nHow many attempts do you want? " # Dil seçimine göre mesajı ayarlar.
    hata1 = "Lütfen pozitif bir sayı girin!" if dil == "tr" else "Please enter a positive number!" # Pozitif sayı hatasını ayarlar.
    hata2 = "Lütfen geçerli bir sayı girin!" if dil == "tr" else "Please enter a valid number!" # Geçerli sayı hatasını ayarlar.
    
    while True: # Geçerli bir giriş yapılana kadar döngüyü sürdürür.
        try: # Girişi tamsayıya çevirme işlemini dener.
            hak = int(input(mesaj)) # Kullanıcıdan hak sayısını alır.
            if hak > 0: # Hak sayısı pozitif ise.
                return hak # Hak sayısını döndürür.
            print(hata1) # Pozitif değilse hata mesajı verir.
        except ValueError: # Giriş tamsayıya çevrilemezse (örneğin metin girilirse).
            print(hata2) # Geçerli sayı hatası verir.

def tahmin_al(harf_sayisi, dil): # Kullanıcıdan geçerli ve doğru uzunlukta tahmin kelimesi alan fonksiyonu tanımlar.
    mesaj = "\nTahmininiz: " if dil == "tr" else "\nYour guess: " # Dil seçimine göre giriş mesajını ayarlar.
    hata1 = f"Lütfen {harf_sayisi} harfli bir kelime girin!" if dil == "tr" else f"Please enter a {harf_sayisi}-letter word!" # Uzunluk hatasını ayarlar.
    hata2 = "Lütfen sadece harf girin!" if dil == "tr" else "Please enter only letters!" # Harf hatasını ayarlar.
    
    while True: # Geçerli bir tahmin alınana kadar döngüyü sürdürür.
        tahmin = input(mesaj).strip() # Kullanıcıdan tahmini alır ve boşlukları siler.
        
        if dil == "tr": # Dil Türkçe ise.
            tahmin = tr_upper(tahmin) # tr_upper ile büyük harfe çevirir.
        else: # Dil İngilizce ise.
            tahmin = tahmin.upper() # Standart upper() ile büyük harfe çevirir.

        if len(tahmin) != harf_sayisi: # Tahminin uzunluğu beklenen harf sayısına eşit değilse.
            print(hata1) # Uzunluk hatası verir.
            continue # Döngünün başına döner.

        kontrol = tahmin # Harf kontrolü için tahmini kontrol değişkenine kopyalar.
        if dil == "tr": # Eğer Türkçe ise, özel harfleri geçici olarak standart karşılıklarına çevirir.
            kontrol = tahmin.replace('Ç', 'C').replace('Ğ', 'G').replace('İ', 'I').replace('Ö', 'O').replace('Ş', 'S').replace('Ü', 'U')
            
        if not kontrol.isalpha(): # Kontrol metni sadece harflerden oluşmuyorsa.
            print(hata2) # Harf hatası verir.
            continue # Döngünün başına döner.

        return tahmin # Geçerli tahmini döndürür.

def tahmini_renklendir(tahmin, hedef_kelime): # Tahmini Wordle kurallarına göre renklendiren fonksiyonu tanımlar.
    renkli_tahmin = "" # Renkli tahminin tutulacağı boş dizeyi tanımlar.
    hedef_harfler = list(hedef_kelime) # Hedef kelimenin harflerini bir listeye kopyalar (frekans/tekrar kontrolü için).
    
    sonuc = [''] * len(tahmin) # Renklendirme sonuçlarını tutmak için tahmin uzunluğunda boş bir liste oluşturur.
    
    for i, harf in enumerate(tahmin): # Tahminin her harfi ve indeksi üzerinde döner (1. Aşama: Yeşil).
        if harf == hedef_kelime[i]: # Harf doğru yerde ise.
            sonuc[i] = YESIL + harf + RESET # Sonuç listesine Yeşil renkli harfi ekler.
            hedef_harfler[i] = None # Hedef harf listesinden bu harfi (konumu) siler/etkisizleştirir.
    
    for i, harf in enumerate(tahmin): # Tahminin her harfi ve indeksi üzerinde tekrar döner (2. Aşama: Sarı/Kırmızı).
        if sonuc[i] == '': # Eğer harf zaten Yeşil olarak işaretlenmemişse.
            if harf in hedef_harfler: # Harf, hedef kelimenin kalan (None olmayan) harfleri arasında varsa.
                sonuc[i] = SARI + harf + RESET # Sonuç listesine Sarı renkli harfi ekler.
                hedef_harfler[hedef_harfler.index(harf)] = None # Sarı olarak işaretlenen harfi de listeden çıkarır (bir harf sadece bir kez sayılır).
            else: # Harf, hedef kelimenin hiçbir yerinde yoksa (veya zaten kullanılmışsa).
                sonuc[i] = KIRMIZI + harf + RESET # Sonuç listesine Kırmızı renkli harfi ekler.
                
    return " ".join(sonuc) # Renkli harfleri aralarına boşluk koyarak birleştirir ve döndürür.

def oyun_tahtasi_goster(tahminler, hak_sayisi, harf_sayisi): # Oyun tahtasını ve durumu gösteren fonksiyonu tanımlar.
    temizle_ekran() # Ekranı temizler.
    print("\n" + "=" * 40) # Üst ayırıcı çizgiyi yazar.

    for tahmin in tahminler: # Önceki tahminleri gösterir.
        print(tahmin)

    kalan_hak = hak_sayisi - len(tahminler) # Kalan hak sayısını hesaplar.
    for _ in range(kalan_hak): # Kalan hak sayısı kadar döner.
        print("_ " * harf_sayisi) # Boş tahmin satırlarını gösterir.

    print("=" * 40) # Alt ayırıcı çizgiyi yazar.

def seviye_oyna(harf_sayisi, hak_sayisi, dil, test_modu): # Tek bir seviyeyi (harf sayısını) oynatan fonksiyonu tanımlar.
    hedef_kelime = kelime_yukle(harf_sayisi, dil) # Hedef kelimeyi yükler.
    
    if hedef_kelime is None: # Kelime yüklenemezse.
        if dil == "tr": # Türkçe mesaj.
            print(f"\n🚫 {harf_sayisi} harfli kelime bulunamadı. Sonraki seviyeye geçiliyor.")
        else: # İngilizce mesaj.
            print(f"\n🚫 No {harf_sayisi}-letter word found. Skipping to the next level.")
        return True # Seviyeyi "geçilmiş" kabul edip True döndürür.

    tahminler = [] # Tahmin geçmişini tutacak boş listeyi oluşturur.

    while len(tahminler) < hak_sayisi: # Haklar bitene kadar döngüyü sürdürür.
        oyun_tahtasi_goster(tahminler, hak_sayisi, harf_sayisi) # Oyun tahtasını gösterir.
        
        if test_modu: # Test modu açıksa.
            print(f"[TEST] Hedef kelime: {hedef_kelime}") # Hedef kelimeyi gösterir.

        tahmin = tahmin_al(harf_sayisi, dil) # Kullanıcıdan tahmini alır.
        renkli_tahmin = tahmini_renklendir(tahmin, hedef_kelime) # Tahmini renklendirir.
        tahminler.append(renkli_tahmin) # Renkli tahmini geçmişe ekler.

        if tahmin == hedef_kelime: # Tahmin, hedef kelimeyi bulduysa.
            oyun_tahtasi_goster(tahminler, hak_sayisi, harf_sayisi) # Son durumu gösterir.
            
            if dil == "tr": # Türkçe kazanma mesajı.
                print(f"\n✨ Tebrikler! Kelimeyi {len(tahminler)} tahminde buldunuz!")
            else: # İngilizce kazanma mesajı.
                print(f"\n✨ Congratulations! You found the word in {len(tahminler)} attempts!")
            return True # Kazanma durumunu True olarak döndürür.

    oyun_tahtasi_goster(tahminler, hak_sayisi, harf_sayisi) # Haklar bittiğinde son tahtayı gösterir.
    
    if dil == "tr": # Türkçe kaybetme mesajı.
        print(f"\n❌ Kaybettiniz! Doğru kelime: {hedef_kelime}")
    else: # İngilizce kaybetme mesajı.
        print(f"\n❌ You lost! The correct word was: {hedef_kelime}")
    return False # Kaybetme durumunu False olarak döndürür.

def tekrar_oyna_sor(dil): # Kullanıcıya tekrar oynama sorusu soran fonksiyonu tanımlar.
    mesaj = "\nTekrar oynamak ister misiniz? (e/h): " if dil == "tr" else "\nDo you want to play again? (y/n): " # Dil seçimine göre mesajı ayarlar.
    hata = "Lütfen 'e' veya 'h' girin!" if dil == "tr" else "Please enter 'y' or 'n'!" # Dil seçimine göre hata mesajını ayarlar.
    
    while True: # Geçerli bir cevap gelene kadar döngüyü sürdürür.
        cevap = input(mesaj).strip().lower() # Girişi alır, boşlukları siler ve küçük harfe çevirir.
        if cevap in ['e', 'y']: # Cevap 'e' veya 'y' ise.
            return True # True döndürür.
        if cevap in ['h', 'n']: # Cevap 'h' veya 'n' ise.
            return False # False döndürür.
        print(hata) # Geçersiz giriş uyarısı verir.

def test_modu_sor(dil): # Kullanıcıya test modu sorusu soran fonksiyonu tanımlar.
    mesaj = "\nTest modu açık olsun mu? (Hedef kelime görünür) (e/h): " if dil == "tr" else "\nEnable test mode? (Target word will be visible) (y/n): " # Dil seçimine göre mesajı ayarlar.
    hata = "Lütfen 'e' veya 'h' girin!" if dil == "tr" else "Please enter 'y' or 'n'!" # Dil seçimine göre hata mesajını ayarlar.
    
    while True: # Geçerli bir cevap gelene kadar döngüyü sürdürür.
        cevap = input(mesaj).strip().lower() # Girişi alır, boşlukları siler ve küçük harfe çevirir.
        if cevap in ['e', 'y']: # Cevap 'e' veya 'y' ise.
            return True # True döndürür.
        if cevap in ['h', 'n']: # Cevap 'h' veya 'n' ise.
            return False # False döndürür.
        print(hata) # Geçersiz giriş uyarısı verir.

def ana_oyun(): # Oyunun ana döngüsünü ve akışını yöneten fonksiyonu tanımlar.
    temizle_ekran() # Başlangıçta ekranı temizler.
    dil = dil_sec() # Dil seçimi yapar.
    temizle_ekran() # Dil seçiminden sonra ekranı tekrar temizler.
    
    if dil == "tr": # Dil Türkçe ise.
        print("=" * 40) # Başlık çizgisini yazar.
        print(" WORDLE OYUNUNA HOŞ GELDİNİZ! ") # Türkçe karşılama mesajını yazar.
        print("=" * 40) # Başlık çizgisini yazar.
        print("\n🟩 Yeşil: Doğru harf, doğru yerde") # Renk açıklamalarını yazar.
        print("🟨 Sarı: Doğru harf, yanlış yerde")
        print("🟥 Kırmızı: Yanlış harf")
    else: # Dil İngilizce ise.
        print("=" * 40) # Başlık çizgisini yazar.
        print(" WELCOME TO WORDLE GAME! ") # İngilizce karşılama mesajını yazar.
        print("=" * 40) # Başlık çizgisini yazar.
        print("\n🟩 Green: Correct letter, correct position") # Renk açıklamalarını yazar.
        print("🟨 Yellow: Correct letter, wrong position")
        print("🟥 Red: Wrong letter")

    test_modu = test_modu_sor(dil) # Test modu durumunu sorar.
    hak_sayisi = hak_sayisi_al(dil) # Kullanıcıdan hak sayısını alır.

    for harf_sayisi in range(4, 9): # 4'ten 8'e kadar (4, 5, 6, 7, 8) harf sayıları için döngü başlatır.
        temizle_ekran() # Seviye başlamadan ekranı temizler.
        print(f"\n{'=' * 40}") # Seviye başlığı çizgisini yazar.
        if dil == "tr": # Türkçe seviye başlığını yazar.
            print(f" SEVİYE: {harf_sayisi} HARFLİ KELİME")
        else: # İngilizce seviye başlığını yazar.
            print(f" LEVEL: {harf_sayisi}-LETTER WORD")
        print(f"{'=' * 40}") # Seviye başlığı çizgisini yazar.
        
        if dil == "tr": # Türkçe devam etme onayı ister.
            input("\nDevam etmek için Enter'a basın...")
        else: # İngilizce devam etme onayı ister.
            input("\nPress Enter to continue...")

        kazandi = seviye_oyna(harf_sayisi, hak_sayisi, dil, test_modu) # Seviye oyununu başlatır.

        if not kazandi: # Seviye kaybedilirse.
            return # Ana oyunu sonlandırır.

    print("\n" + "=" * 40) # Tüm seviyeler tamamlandığında ayırıcı çizgi yazar.
    if dil == "tr": # Türkçe tebrik mesajı.
        print(" TEBRİKLER! TÜM SEVİYELERİ TAMAMLADINIZ! 🏆")
    else: # İngilizce tebrik mesajı.
        print(" CONGRATULATIONS! YOU COMPLETED ALL LEVELS! 🏆")
    print("=" * 40) # Ayırıcı çizgi yazar.

    if tekrar_oyna_sor(dil): # Tüm seviyeler bittikten sonra tekrar oynama sorusu sorar.
        ana_oyun() # Evet ise ana oyunu yeniden başlatır.
    else: # Hayır ise.
        if dil == "tr": # Türkçe veda mesajı.
            print("\n👋 Görüşmek üzere!")
        else: # İngilizce veda mesajı.
            print("\n👋 See you later!")

if __name__ == "__main__": # Kod doğrudan çalıştırıldığında (import edilmediğinde).
    ana_oyun() # ana_oyun fonksiyonunu çağırarak oyunu başlatır.
