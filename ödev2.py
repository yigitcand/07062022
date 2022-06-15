import time
savedusername="test"
savedpassword="123"
sayac=yeniad=yenisifre=yenisifretekrar=0
giris=f"""
          ▄▄           ▄▄         
          ██           ██         
                                  
 ▄█▀████████ ▀███▄███▀███  ▄██▀███
▄██  ██   ██   ██▀ ▀▀  ██  ██   ▀▀
▀█████▀   ██   ██      ██  ▀█████▄
██        ██   ██      ██  █▄   ██
 ███████▄████▄████▄  ▄████▄██████▀
█▀     ██                         
██████▀                           
"""
while True:
    print(giris)
    kad=input("Kullanıcı adınızı giriniz")
    ksifre=input("Şifrenizi giriniz")
    if (kad==savedusername and ksifre==savedpassword) or (kad==yeniad and ksifre==yenisifre):
        print("Giriş Başarılı")
        break
    else:
        while True:
            cevap=input("Hesap bulunamadı. Yeni bir hesap yaratmak ister misiniz? E/H").upper()
            if sayac==3:
                print("Çok fazla giriş denemesi yaptınız, lütfen sonra deneyiniz")
                time.sleep(3)
                sayac=0
                break
            elif cevap=="H":
                print("Peki...")
                sayac+=1
                continue
            elif cevap=="E":
                yeniad=input("Yeni kullanıcı adınızı giriniz")
                while True:
                    yenisifre=input("Yeni şifrenizi giriniz")
                    yenisifretekrar=input("Yeni şifrenizi tekrar giriniz")
                    if yenisifre==yenisifretekrar:
                        print("Hesap yaratımı başarılı!")
                        break
                    else:
                        print("Şifreler birbirini tutmuyor, lütfen tekrar deneyiniz")
                        continue
                break
            else:
                print("Evet veya hayır cevabını vermeniz lazım")
                sayac+=1
                continue