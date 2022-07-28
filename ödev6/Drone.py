from Base import Base
class Drone(Base):
    def __init__(self):
        super().__init__()
        self.ucus_mesafesi = str()
        self.sarj_suresi = str()
        self.kamera_cozunurlugu = str()
    def UrunYaz(self):
        super().UrunYaz()
        dosya = open("Ürünler.txt", mode="a+", encoding="utf-8")
        dosya.write(f"""
Uçuş Mesafesi:      {self.ucus_mesafesi}
Sarj Süresi:        {self.sarj_suresi}
Kamera Çözünürlüğü: {self.kamera_cozunurlugu}
""")
        dosya.close()
    def UrunListele(self):
        super().UrunListele()
    def UrunSil(self):
        super().UrunSil()
    def BilgiGuncelle(self):
        super().BilgiGuncelle()
        self.ucus_mesafesi=int(input("Uçuş mesafesi:"))
        self.sarj_suresi=input("Sarj süresi:")
        self.kamera_cozunurlugu=input("Kamera çözünürlüğü:")
    def BilgiYaz(self):
        super().BilgiYaz()
        print(f"""
Uçuş Mesafesi:      {self.ucus_mesafesi}
Sarj Süresi:        {self.sarj_suresi}
Kamera Çözünürlüğü: {self.kamera_cozunurlugu}""")
    def BilgiSil(self):
        super().BilgiSil()
        self.ucus_mesafesi=0
        self.sarj_suresi=""
        self.kamera_cozunurlugu=""






