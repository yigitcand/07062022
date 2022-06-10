ad="test"
sifre="test123"
adgiris=input("Adınızı giriniz")
sifregiris=input("Şifrenizi giriniz")
if ad==adgiris and sifre==sifregiris: print("Giriş başarılı!")
elif ad==adgiris and sifre!=sifregiris:
    cevapsifre=input("Parolanız yanlış. Sıfırlamak ister misiniz?")
    if cevapsifre=="hayir": print("PEKİ!!!")
    elif cevapsifre=="evet":
        sifirlanmissifre=input("Yeni şifrenizi giriniz")
        print("Yeni şifreniz oluşturulmuştur!")
else:
    cevap=input("Hesap bulunamadı, yeni hesap yapmak ister misiniz?")
    if cevap=="hayır": print("PEKİ!!!")
    elif cevap=="evet":
        yeniad=input("Yeni kullanıcı isminizi giriniz")
        yeniemail=input("Yeni e-mailinizi giriniz")
        yenisifre=input("Yeni şifrenizi giriniz")
        yenisifretekrar=input("Yeni şifrenizi tekrar giriniz")
        if yenisifre==yenisifretekrar: print("Hesap yaratımı başarılı!")
        else: print("Şifreleriniz aynı değil, lütfen kontrol ediniz")