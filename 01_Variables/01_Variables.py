########################### ALGORİTMA ##################################

"""
ÖRNEK-1 : Kullanıcı tarafından belirlenen 3 farklı sayının ortalamasını alalım.
"""

"""
1. Başla
2. Birinci sayıyı al
3. İkinci sayıyı al
4. Üçüncü sayıyı al
5. üçünü topla ve sonucu 3 e böl
6. Ortalamayı ekrana yaz
7.Bitir
"""

#
# .askdaslkd
# lşaskdşlaskd
# çöljasdklşjasd
# jnaslkşdjaslkd
# klajsdlkjasdlkasüklşjasdşlas


# DEĞİŞKEN KAVRAMI
kaleci = "Mehmet Nuri"
print( kaleci )

#  snake_case
#  camelCase
# PascalCase
# FULLCASE
# kebab-case

# Yanlış isimlendirmeler:  5sayi, ?sayi, ad soyad, sayi?, sayi!
# Doğru isimlendirmeler:   sayi5, sayi, ad_soyad, adSoyad, sayi, sayi_

# değişken tanımlama
# değişkenin adi = değer

# tam sayı veri tipi
# - sonsuz 0 + sonsuza kadar

sayi1 = 5
sayi2 = 6

print( type( sayi1 ) )  # tam sayi int

# Noktalı veri tipi
sayi3 = 10.45
print( type( sayi3 ) )  # noktalı sayi float

# Metinsel veri tipi (str)
adim = "Merhaba Python ile başlangıç yaptık"
ders_kodu = 'P'

print( adim )
print( ders_kodu )

print( type( adim ) )
print( type( ders_kodu ) )

# Mantıksal Veri Tipi Boolean
arabasi_var_mi = True
ucagi_var_mi = False

# int ve float örneği
# bir öğrencinin iki notunun ortalamasını ekrana yazdıran program.

not1 = 70
not2 = 60
ortalama = (not1 + not2) / 2
print( ortalama )

sayi = "120"
sayi2 = "3910"
toplam = sayi + sayi2
print( toplam )

### '+' operatörü integer tiplerde toplama işlemi gerçekleştirirken,
# string tiplerde birleştirme işlemi gerçekleştirir.

sayi = 120
sayi2 = 3910
toplam = sayi + sayi2
print( toplam )

ad = "Mehmet Nuri"
soyad = "Öztürk"

print( ad + soyad )

c1 = c2 = c3 = 15
print( c2 )
print( c1 )
print( c3 )

d1, d2, d3 = 12, 15, 18
print( d1, d2, d3 )
print( "d1 in değeri:", d1 )
print( f"d1 in değeri: {d1}" )
print( "d1 in değeri: {}".format( d1 ) )

ad, soyad, yas = "Mehmet Nuri", "Öztürk", 28
print( f"ADI:{ad}, SOYADI:{soyad}, YAŞI:{yas}" )

x1 = 5
x2 = 7
print( "Önceki Durumu" )
print( x1 )
print( x2 )

print( "Sonraki Durumu" )
x2 = x1
print( x1 )
print( x2 )

##### KAÇIŞ KARAKTERLERİ #####
# \n new line
# \t TAB
yazi = "Merhaba\n\n\nDünya"
print( yazi )

yazi = "Merhaba\t\t\tDünya"
print( yazi )

print( "Bu", "Gün", "Hava Güneşli", sep="x" )

print( "Bu", "Gün", "Hava Güneşli", end="x" )

bilgilerim = f"""
        Merhaba, ben {ad} {soyad}
        Şehir:  İstanbul
"""

print( bilgilerim )
print( """
merhabalar 
bu 
gun
ilk
python 
dersi
"""
       )

## Kullanıcıdan veri almak için 'input'

kullanici_adi = input( "Lütfen kullanıcı adınızı giriniz: " )  # String
print( kullanici_adi )
