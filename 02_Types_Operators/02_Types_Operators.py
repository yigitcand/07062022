# x = int(input( "Lütfen bir sayı girin" ))
# print( x )
# print( type( x ) )
#
# sonuc = x + 12
# print( sonuc )

### 3 kişinin yaşlarını dışarıdan alıp toplamını ekrana yazıdırınız.

# Toplama  +
# Çıkarma  -
# Çarpma   *
# Bölme    /
# Mod Alma %

# x1 = int(input("Birinci yaş"))
# x2 = int(input("İkinci yaş"))
# x3 = int(input("Üçüncü yaş"))
#
# toplam =  x1+x2+x3
# print(toplam)
#
# dogum_yili =  input("Lütfen dogum yilinizi giriniz")
#
# yas = 2022 - int(dogum_yili)
# print(yas)
#

#
# x1 =  int(input("Bölünecek sayıyı girin"))
# x2 =  int(input("Bölen sayıyı girin"))
#
# kalan =  x1 % x2 # kalan
# bolum =  x1/x2 #bölüm
#
# sonuc =  f"""
#         Bölünen sayı            {x1}
#         Bölen sayı              {x2}
#         Kalan                   {kalan}
#         Bölüm                   {bolum}
# """
# print(sonuc)

# ASCII TABLOSU

harf = chr( 67 )
print( harf )

karakter = ord( "C" )
print( karakter )

# del karakter # ramden karakter değişkenini sil
print( karakter )

# SORU Klavyeden girilen 2 sayıdan 1. nin büyük olup olmadığını ekrana yazdıran kod..

#  < , >, >=, <=, != ,  ==

# sayi1 = int( input( "Birinci Sayi" ) )
# sayi2 = int( input( "İkinci Sayi" ) )
# print( sayi2 > sayi1 )  # boolean dönmesi gerekiyor
# print( type(sayi2 > sayi1 ))  # boolean dönmesi gerekiyor
#


###  OPERATÖRLER ###

sayi = 5
print( sayi )

# sayi = sayi + 5 #uzun hali
sayi += 5  # kısa hali
print( sayi )

# İşlemli Atama Operatörü
sayi -= 5
print( sayi )

sayi *= 10
print( sayi )

sayi /= 2
print( sayi )

# Aritmatik Operatörler
"""
    +,-,* :toplama,çıkarma,çarpma
    /     :ondalıklı bölme (10/4=2.5)
    //    :bölümün tamsayı kısmını verir (10//4=2)
    **    :üs alma(5**2=25)
"""

# x1 = int( input( "Bölünecek sayıyı girin" ) )
# x2 = int( input( "Bölen sayıyı girin" ) )
#
# kalan = x1 % x2  # kalan
# bolum = x1 / x2  # bölüm
# tam_bolum = x1 // x2  # tam bölüm
#
# sonuc = f"""
#         Bölünen sayı            {x1}
#         Bölen sayı              {x2}
#         Kalan                   {kalan}
#         Bölüm                   {bolum}
#         Tam Bölüm               {tam_bolum}
# """
# print( sonuc )

sayi1 = 100
sayi2 = 200

esitlik_kontrol =  sayi1 == sayi2
esitlik_kontrol2 = sayi1 is sayi2
esitlik_kontrol3 =  sayi is not sayi2  # not keyword'ü ifadeyi ters çevirir.
esitlik_kontrol4 =  sayi != sayi2

print(esitlik_kontrol)
print(esitlik_kontrol2)
print(esitlik_kontrol3)
print(esitlik_kontrol4)

ilce = "kadiköy"

print("adi" in  ilce) # in keyword içeriyor mu?

## SORU: Kullanıcıdan alınan 1.sayının kullanıcının girdiği
# 2. sayıya kuvvetini hesaplayarak ekrana yazdıran prog.

taban = int(input("Lütfen tabanı giriniz: "))
us = int(input("Lütfen üssü giriniz: "))

sonuc = taban**us
print(f"{taban} sayısının {us}  ussunun degeri = {sonuc}")
