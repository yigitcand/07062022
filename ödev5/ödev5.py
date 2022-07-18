from os import path, remove
from time import sleep
while True:
    print("""
▀██                                     ▀██      ▀██   ██            ██          
 ██ ▄▄     ▄▄▄    ▄▄▄▄    ▄▄▄ ▄   ▄▄▄▄   ██    ▄▄ ██  ▄▄▄  ▄▄ ▄▄▄   ▄▄▄  ▄▄▄▄▄▄  
 ██▀ ██  ▄█  ▀█▄ ██▄ ▀   ██ ██  ▄█▄▄▄██  ██  ▄▀  ▀██   ██   ██  ██   ██  ▀  ▄█▀  
 ██  ██  ██   ██ ▄ ▀█▄▄   █▀▀   ██       ██  █▄   ██   ██   ██  ██   ██   ▄█▀    
▄██▄ ██▄  ▀█▄▄█▀ █▀▄▄█▀  ▀████▄  ▀█▄▄▄▀ ▄██▄ ▀█▄▄▀██▄ ▄██▄ ▄██▄ ██▄ ▄██▄ ██▄▄▄▄█ 
                        ▄█▄▄▄▄▀                                                                                             
""")
    giris=int(input("""
PERSONEL EKLEMEK İÇİN       1
PERSONEL GÜNCELLEMEK İÇİN   2
PERSONEL SİLMEK İÇİN        3
PERSONEL LİSTELEMEK İÇİN    4

ÇIKIŞ İÇİN                  0                                                                      
"""))
    if giris==1:
        personelsayi=int(input("Eklenicek personel sayısını giriniz"))
        for i in range(personelsayi):
            isim=input("İsim giriniz")
            soyisim=input("Soyisim giriniz")
            dogumtarihi=int(input("Doğum tarihini giriniz"))
            personelbolum=int(input("""Personel bölümünü giriniz:
İnsan Kaynakları için   1
Muhasebe için           2
Bilgi İşlem için        3
"""))
            if personelbolum==1:
                dosya = open(str(isim) + ".txt", mode="a+", encoding="utf8")
                dosya.write(str(isim) + "\t\t" + str(soyisim) + "\t\t" + str(dogumtarihi) + "\n")
                dosya.write("Personel bölümü : İnsan Kaynakları\n")
                dosya.close()
                dosya=open("IK.txt", mode="a+", encoding="utf8")
                dosya.write(str(isim) + "\t\t" + str(soyisim) + "\t\t" + str(dogumtarihi) + "\n")
                dosya.close()
            elif personelbolum==2:
                dosya = open(str(isim) + ".txt", mode="a+", encoding="utf8")
                dosya.write(str(isim) + "\t\t" + str(soyisim) + "\t\t" + str(dogumtarihi) + "\n")
                dosya.write("Personel bölümü : Muhasebe\n")
                dosya.close()
                dosya = open("MHSB.txt", mode="a+", encoding="utf8")
                dosya.write(str(isim) + "\t\t" + str(soyisim) + "\t\t" + str(dogumtarihi) + "\n")
                dosya.close()
            elif personelbolum==3:
                dosya = open(str(isim) + ".txt", mode="a+", encoding="utf8")
                dosya.write(str(isim) + "\t\t" + str(soyisim) + "\t\t" + str(dogumtarihi) + "\n")
                dosya.write("Personel bölümü : Bilgi İşlem\n")
                dosya.close()
                dosya = open("BI.txt", mode="a+", encoding="utf8")
                dosya.write(str(isim) + "\t\t" + str(soyisim) + "\t\t" + str(dogumtarihi) + "\n")
                dosya.close()
            else:
                print("Hatalı seçim, tekrar deneyiniz")
                break
    elif giris==2:
        degisim=input("Değiştirmek istediğiniz personelin adını giriniz")
        dosya=open(str(degisim)+".txt", mode="w+", encoding="uft8")
        yeniisim=input("Yeni isim giriniz")
        yenisoyisim=input("Yeni soyisim giriniz")
        yenidogumtarihi=int(input("Yeni doğum tarihi giriniz"))
        dosya.write(str(yeniisim)+"\t\t"+str(yenisoyisim)+"\t\t"+str(yenidogumtarihi)+"\n")
        print("Veriler güncellenmiştir. Eski veriler silinmiştir")
        dosya.close()
    elif giris==3:
        silinen=input("Silmek istediğiniz dosyayı yazınız")
        if path.exists(str(silinen)+".txt"):
            cevap=input("Silmek istediğinizden emin misiniz? E/H").upper()
            if cevap=="E":
                remove(str(silinen)+".txt")
                print("Dosya silindi, geri dönülüyor")
            elif cevap=="H":
                print("Geri dönülüyor")
            else: print("Hatalı seçim, tekrar deneyiniz")
        else: print("Dosya yok, tekrar deneyiniz")
    elif giris==4:
        listeleme=int(input("""Hangi bölümün listesini istersiniz?
İnsan Kaynakları için   1
Muhasebe için           2
Bilgi İşlem için        3
"""))
        if listeleme==1:
            if path.exists("IK.txt"):
                dosya=open("IK.txt",mode="r",encoding="utf8")
                insankaynaklari=dosya.readlines()
                for i in insankaynaklari:
                    print(i)
                    sleep(5)
            else:
                print("Dosya yok, geri dönülüyor")
        elif listeleme==2:
            if path.exists("MHSB.txt"):
                dosya=open("MHSB.txt",mode="r",encoding="utf8")
                muhasebe=dosya.readlines()
                for i in muhasebe:
                    print(i)
                    sleep(5)
            else: print("Dosya yok, geri dönülüyor")
        elif listeleme==3:
            if path.exists("BI.txt"):
                dosya=open("BI.txt",mode="r",encoding="utf8")
                bilgiislem=dosya.readlines()
                for i in bilgiislem:
                    print(i)
                    sleep(5)
            else:
                print("Dosya yok, geri dönülüyor")
        else: print("Hatalı seçim, geri dönülüyor")
    elif giris==0: break
    else: print("Hatalı seçim, tekrar deneyiniz")
