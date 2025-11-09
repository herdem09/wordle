import random
import os

# Kelime listeleri
dort = ("Masa", "Ayna", "Vazo", "Kase", "Maşa", "Sıra", "Örtü", "Örgü", "Askı", "Elek", "Priz", "Kapı", "İğne", "Odun", "Halı", "Alçı", "Atkı", "Etek", "Bluz", "Küpe", "Takı", "Deve", "Keçi", "Kuzu", "Enik", "Eşek", "Kene", "Pire", "Dana", "Öküz", "İnek", "Fare", "Kurt", "Roka", "Tere", "Üzüm", "Ayva", "Elma", "Erik", "Kivi", "Pazı", "İğde", "Şiir", "Öykü", "Şair", "Kıta", "Dize", "Naat", "Mani", "Atıf", "Övme", "Örme", "Alma", "Ekme", "Atma", "Akma", "Açma", "Etme", "Ezme", "İçme", "Uzun", "Kısa", "Uslu", "Akil", "Katı", "Ilık", "Sert", "Adil", "Baki", "Alık", "Asık", "Açık", "Evli", "Mini", "Eski", "Yeni", "Gani", "Razı", "Enli", "Duru", "Hata", "Hile", "Usul", "Tarz", "Yeti", "Yakı", "Alem", "Adim", "Mali", "Mazi", "Ayıp", "Azık", "Ufuk", "Anne", "Baba", "Oğul", "Dede", "Ukde", "Işık", "Rıza", "Rest", "Geda", "Maaş", "Araf", "Okul", "Oyun", "Algı", "Saki", "Dide", "Dara", "Bade", "Dört", "Altı", "Yedi", "Çene", "Çalı", "Çatı", "Bazı", "Asla", "Kare", "Kura", "Kart", "Hane", "Tane", "Pano", "Solo", "Koro", "Balo", "Çile", "Bela")
bes = ("Adana", "Acaba", "Acele", "Abide", "Bakım", "Balık", "Bacak", "Bahar", "Cıvık", "Cüsse", "Cübbe", "Cezve", "Çocuk", "Çuval", "Çamur", "Çubuk", "Direk", "Dayak", "Darbe", "Eşarp", "Ecdat", "Erkek", "Endam", "Ender", "Funda", "Fular", "Fıkra", "Güreş", "Gümüş", "Günah", "Görev", "Hafta", "Haram", "Havva", "Horoz", "İptal", "İpucu", "İshal", "İlham", "Irgat", "Issız", "Japon", "Jilet", "Kömür", "Korna", "Korse", "Kayık", "Levha", "Lavaş", "Lisan", "Lider", "Metre", "Makas", "Merak", "Miras", "Nabız", "Nezle", "Narin", "Namaz", "Omlet", "Oğlan", "Önlük", "Ödünç", "Poşet", "Pasak", "Polis", "Rimel", "Rüküş", "Savaş", "Sinir", "Şafak", "Şurup", "Taviz", "Tepsi", "Uysal", "Üçgen", "Vişne", "Yakın", "Zıbın", "Afaki", "Açlık", "Abiye", "Abbas", "Balon", "Bahri", "Bahçe", "Cacık", "Camcı", "Cıbıl", "Cümle", "Çöpçü", "Çürük", "Çinli", "Çinko", "Çözüm", "Dilim", "Daimi", "Dilek", "Dışkı", "Ezber", "Evlat", "Enfes", "Fosil", "Felek", "Gayet", "Giyim", "Gazoz", "Hamak", "Hoşaf", "Hamsi", "İnmek", "İnkar", "İbraz", "Irkçı", "Ilgaz", "Jokey", "Jarse", "Kredi", "Kalın", "Kablo", "Lüzum", "Lotus", "Leğen", "Mevla", "Masal", "Melez", "Nişan", "Nalan", "Ninni", "Oğlak", "Övmek", "Ördek", "Pilot", "Posta", "Rampa", "Roman", "Sakız", "Savcı", "Şifre", "Tekne", "Uzman", "Üzgün", "Vakıf", "Yalın", "Zehir")
altı = ("Amatör", "Antika", "Adliye", "Bakkal", "Balkon", "Beceri", "Cazibe", "Coşkun", "Çakmak", "Çeviri", "Demlik", "Defter", "Devlet", "Emekli", "Elveda", "Fiziki", "Formül", "Fosfor", "Galeri", "Galeta", "Gömlek", "Hayvan", "Haylaz", "Hırsız", "İbadet", "İkilem", "İlişki", "Izgara", "Jakuzi", "Kanepe", "Kangal", "Karpuz", "Kısmet", "Lastik", "Medeni", "Makbuz", "Mangal", "Naylon", "Nafaka", "Okumak", "Otoyol", "Öpücük", "Özenti", "Pastel", "Pancar", "Parola", "Rafine", "Saygın", "Seçmen", "Sinyal", "Şefkat", "Tabaka", "Teşhir", "Tırnak", "Turizm", "Terlik", "Ulusal", "Üzüntü", "Vesile", "Vernik", "Yıldız", "Yüksük", "Yorgan", "Zabıta", "Zanaat", "Abdest", "Ahiret", "Akıllı", "Balayı", "Bakiye", "Bitter", "Cüzdan", "Cömert", "Çeyrek", "Çember", "Çıplak", "Dakika", "Dalgıç", "Defolu", "Dikkat", "Eczacı", "Emanet", "Erişte", "Filtre", "Fincan", "Finans", "Gofret", "Gözlük", "Güncel", "Haksız", "Hamile", "Hangar", "İçecek", "İnşaat", "İyilik", "Ilıman", "Jeolog", "Kafein", "Kaktüs", "Kamyon", "Kirpik", "Kraker", "Laktoz", "Lateks", "Meclis", "Merkez", "Migren", "Nefret", "Numune", "Oklava", "Otogar", "Özveri", "Önemli", "Piyasa", "Peynir", "Protez", "Parfüm", "Rustik", "Rüzgar", "Saniye", "Sağdıç", "Sağlam", "Şamdan", "Tablet", "Toptan", "Tropik", "Tabiat", "Termal", "Ulaşım", "Ülkücü", "Üretim", "Vadeli", "Vizyon", "Yaprak", "Yazlık", "Yüklük", "Zahmet", "Zincir", "Zeybek", "Havalı", "Yanmak", "Eğitim", "Kazanç", "Kapalı", "Yaralı", "Lezzet", "Pusula", "Yazıcı", "Makine", "Kumral", "Kumsal")
yedi = ("Adaptör", "Akademi", "Başvuru", "Besleme", "Cezerye", "Cızırtı", "Çalıntı", "Dayanma", "Defaten", "Emniyet", "Felsefe", "Gezegen", "Gıyaben", "Hasetçi", "Halkevi", "İstisna", "İzdivaç", "İzmarit", "Islahat", "Isparta", "Jüpiter", "Jeoloji", "Kaburga", "Kaçakçı", "Kanguru", "Kadınsı", "Karizma", "Langırt", "Lökosit", "Madalya", "Maruzat", "Muallim", "Namuslu", "Nezaket", "Organik", "Olaysız", "Ödeşmek", "Öksürme", "Paraşüt", "Paravan", "Parazit", "Radikal", "Rafadan", "Seccade", "Sivilce", "Sömürge", "Şaibeli", "Şaheser", "Taharet", "Takıntı", "Teminat", "Ucuzluk", "Unutmak", "Üflemek", "Ürperti", "Vezneci", "Vilayet", "Viyadük", "Yabancı", "Yadigar", "Yargıcı", "Zararlı", "Derslik", "Öğrenci", "Muallim", "Biyolog", "Bakteri", "Malumat", "Saldırı", "Serenat", "Mükafat", "Feribot", "Gürültü", "Yetenek", "Tecelli", "Nezaket", "Sahavet", "Hamiyet", "Dopdolu", "Rehavet", "Teselli", "Manolya", "Romancı", "Meziyet", "İstifra", "İhtişam", "İttifak", "Istırap", "İmtiyaz", "Trajedi", "Tiyatro", "Aslında", "Tapınak", "İltihap", "Müessir", "Payidar", "Sayısal", "Realist", "Muhalif", "Güvenli", "Faydalı", "Mutabık", "Muvafık", "Tesirli", "Detaylı", "Mürebbi", "Yumuşak", "Mübarek", "Değişik", "Utangaç", "Saygılı", "Çeşitli", "Yararlı", "Gururlu", "Dairevi", "Manidar", "Alışkın", "Kasıntı", "Mutedil", "Müşteki", "Tahmini", "İşgüzar", "Şeftali", "Patates", "Kereviz", "Muşmula", "Domates", "Avokado", "Börülce", "Makarna", "Dereotu", "Ispanak", "Brokoli", "Kukumav", "Pelikan", "Örümcek", "Penguen", "Balaban", "Papağan", "Karınca", "Kızkuşu", "Telefon", "Mobilya", "Tencere", "Firkete", "Karyola", "Mengene", "Işıldak", "Testere", "Askılık", "Ağlanma", "Yakınma", "Övünmek", "Sevinme", "Çekişme", "Katılma", "Yitirme", "Boşanma", "Bağırma", "Evlenme", "Bırakma", "Çağırma", "Giyinme", "Suçlama", "Başlama", "Bitirme", "Dağıtma", "Toplama", "Besleme", "Kapanma", "Söyleme", "Dağılma", "Abartma", "Dadanma")
sekiz = ("Ademoğlu", "Akortsuz", "Albatros", "Alıkoyma", "Alkolizm", "Altıntop", "Anakonda", "Antoloji", "Arkeolog", "Armonika", "Aromasız", "Aromatik", "Astrolog", "Astronom", "Astronot", "Atıyorum", "Atmasyon", "Atmosfer", "Ayakkabı", "Baloncuk", "Balonsuz", "Banyosuz", "Barkodlu", "Bastoncu", "Bastonlu", "Begonvil", "Bergamot", "Biyoloji", "Biyosfer", "Bocalama", "Bodurluk", "Boğdurma", "Boğuşmak", "Boğulmak", "Bollaşma", "Bollatma", "Bolşevik", "Bolvadin", "Bonboncu", "Bonkörce", "Bostancı", "Boşaltım", "Boşanmak", "Boşboğaz", "Boşnakça", "Boyahane", "Boyatmak", "Boykotçu", "Boylamak", "Boyunluk", "Boyutsuz", "Bozahane", "Bozarmak", "Bozdurma", "Bozguncu", "Bozkırlı", "Bozulmak", "Bozuşmak", "Bronşçuk", "Bungalov", "Bürokrat", "Coğrafya", "Coşturma", "Çikolata", "Çirozluk", "Çobanlık", "Çobansız", "Çocukluk", "Çocuksuz", "Çoğalmak", "Çoğaltan", "Çoğaltım", "Çoğunluk", "Çokçuluk", "Çoksamak", "Çolaklık", "Çorbalık", "Çoraklık", "Çopurluk", "Dedikodu", "Defolmak", "Demagoji", "Demokrat", "Depolama", "Depozito", "Difüzyon", "Diksiyon", "Doğallık", "Doğramak", "Doğrudan", "Doğruluk", "Doğuştan", "Doğumevi", "Dokumacı", "Dokunmak", "Dokuzgen", "Dolambaç", "Dolaşmak", "Dolmuşçu", "Dominant", "Doluşmak", "Dondurma", "Dosdoğru", "Doyumsuz", "Ekolojik", "Endokrin", "Endoskop", "Ergonomi", "Espresso", "Etnoloji", "Faytoncu", "Ferforje", "Filoloji", "Flamenko", "Goygoycu", "Hemofili", "Hemoroit", "Hidrofil", "İdiopati", "İskorpit", "Jeofizik", "Kalantor", "Kalemlik", "Kantaron", "Karambol", "Karbonat", "Karbonit", "Kartoncu", "Kategori", "Kerpeten", "Kitaplık", "Klorofil", "Koçlanma", "Kodlamak", "Komplike", "Komposto", "Konçerto", "Kulaklık", "Lejyoner", "Lokalize", "Marangoz", "Merdiven", "Metropol", "Milyoner", "Montajcı", "Morarmak", "Motorize", "Narkozcu", "Nostalji", "Okunaklı", "Olasılık", "Olumlama", "Onaylama", "Ovalamak", "Pansiyon", "Personel", "Porsiyon", "Romantik", "Sandalye", "Semizotu")


# ANSI renk kodları
KIRMIZI = '\033[91m'
SARI = '\033[93m'
YESIL = '\033[92m'
RESET = '\033[0m'

# Türkçe karakter dönüşümleri
TR_UPPER = str.maketrans('abcçdefgğhıijklmnoöprsştuüvyz', 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ')
TR_LOWER = str.maketrans('ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ', 'abcçdefgğhıijklmnoöprsştuüvyz')

def tr_upper(metin):
    """Türkçe karakterlere uygun büyük harf dönüşümü"""
    return metin.translate(TR_UPPER)

def tr_lower(metin):
    """Türkçe karakterlere uygun küçük harf dönüşümü"""
    return metin.translate(TR_LOWER)

def temizle_ekran():
    os.system('cls' if os.name == 'nt' else 'clear')

def kelime_yukle(harf_sayisi):
    match int(harf_sayisi):
        case 4:
            return tr_lower(random.choice(dort))
        case 5:
            return tr_lower(random.choice(bes))
        case 6:
            return tr_lower(random.choice(altı))
        case 7:
            return tr_lower(random.choice(yedi))
        case 8:
            return tr_lower(random.choice(sekiz))

def hak_sayisi_al():
    while True:
        try:
            hak = input("\nKaç hak istersiniz? ")
            hak = int(hak)
            if hak > 0:
                return hak
            else:
                print("Lütfen pozitif bir sayı girin!")
        except:
            print("Lütfen geçerli bir sayı girin!")

def tahmin_al(harf_sayisi):
    while True:
        tahmin = input(f"\nTahmininiz: ").strip()
        tahmin = tr_lower(tahmin)

        if len(tahmin) != harf_sayisi:
            print(f"Lütfen {harf_sayisi} harfli bir kelime girin!")
            continue

        if not tahmin.replace('ç', 'c').replace('ğ', 'g').replace('ı', 'i').replace('ö', 'o').replace('ş', 's').replace('ü', 'u').isalpha():
            print("Lütfen sadece harf girin!")
            continue

        return tahmin

def tahmini_renklendir(tahmin, hedef_kelime):
    renkli_tahmin = ""
    hedef_harfler = list(hedef_kelime)

    for i, harf in enumerate(tahmin):
        if harf == hedef_kelime[i]:
            renkli_tahmin += YESIL + tr_upper(harf) + RESET
            hedef_harfler[i] = None
        elif harf in hedef_harfler:
            renkli_tahmin += SARI + tr_upper(harf) + RESET
        else:
            renkli_tahmin += KIRMIZI + tr_upper(harf) + RESET

        renkli_tahmin += " "

    return renkli_tahmin

def oyun_tahtasi_goster(tahminler, hak_sayisi, harf_sayisi):
    temizle_ekran()
    print("\n" + "=" * 40)

    for tahmin in tahminler:
        print(tahmin)

    kalan_hak = hak_sayisi - len(tahminler)
    for i in range(kalan_hak):
        print("_ " * harf_sayisi)

    print("=" * 40)

def seviye_oyna(harf_sayisi, hak_sayisi):
    hedef_kelime = kelime_yukle(harf_sayisi)
    tahminler = []

    while len(tahminler) < hak_sayisi:
        oyun_tahtasi_goster(tahminler, hak_sayisi, harf_sayisi)
        print(f"[TEST] Seçilen kelime: {tr_upper(hedef_kelime)}")

        tahmin = tahmin_al(harf_sayisi)

        if tahmin == hedef_kelime:
            renkli_tahmin = tahmini_renklendir(tahmin, hedef_kelime)
            tahminler.append(renkli_tahmin)
            oyun_tahtasi_goster(tahminler, hak_sayisi, harf_sayisi)
            print(f"\n✨ Tebrikler! Kelimeyi {len(tahminler)} tahminde buldunuz!")
            return True
        else:
            renkli_tahmin = tahmini_renklendir(tahmin, hedef_kelime)
            tahminler.append(renkli_tahmin)

    oyun_tahtasi_goster(tahminler, hak_sayisi, harf_sayisi)
    print(f"\n❌ Kaybettiniz! Doğru kelime: {tr_upper(hedef_kelime)}")
    return False

def tekrar_oyna_sor():
    while True:
        cevap = input("\n1. Tekrar başlamak\n2. Çıkış yapmak\nSeçiminiz (1/2): ").strip()
        if cevap == "1":
            return True
        elif cevap == "2":
            return False
        else:
            print("Lütfen 1 veya 2 seçin!")

def ana_oyun():
    print("=" * 40)
    print(" WORDLE OYUNUNA HOŞ GELDİNİZ! ")
    print("=" * 40)

    hak_sayisi = hak_sayisi_al()

    for harf_sayisi in range(4, 9):
        temizle_ekran()
        print(f"\n{'=' * 40}")
        print(f" SEVİYE: {harf_sayisi} HARFLİ KELİME")
        print(f"{'=' * 40}")
        input("\nDevam etmek için Enter'a basın...")

        kazandi = seviye_oyna(harf_sayisi, hak_sayisi)

        if not kazandi:
            if tekrar_oyna_sor():
                ana_oyun()
                return
            else:
                print("\n👋 Görüşmek üzere!")
                return

    print("\n" + "=" * 40)
    print(" TEBRİKLER! TÜM SEVİYELERİ TAMAMLADINIZ! 🏆")
    print("=" * 40)

    if tekrar_oyna_sor():
        ana_oyun()
    else:
        print("\n👋 Görüşmek üzere!")

if __name__ == "__main__":
    ana_oyun()
