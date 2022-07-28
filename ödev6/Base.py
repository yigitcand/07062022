from abc import ABC, abstractmethod
from os import path, remove
class Base(ABC):
    def __init__(self):
        self.isim = str()
        self.fiyat = float()
        self.marka = str()
        self.model = str()
        self.puan = float()
    @abstractmethod
    def UrunYaz(self):
        dosya = open("Ürünler.txt", mode="a+", encoding="utf-8")
        dosya.write(self.isim+"\n")
        dosya.write(f"""İsim:               {self.isim}
Fiyat:              {self.fiyat}
Marka:              {self.marka}
Model:              {self.model}
Puan:               {self.puan}""")
        dosya.close()
    @abstractmethod
    def UrunListele(self):
        dosya = open("Ürünler.txt", mode="r", encoding="utf-8")
        print(dosya.read())
        dosya.close()
    @abstractmethod
    def UrunSil(self):
        try:
            cevap = input("Tüm ürünler silinecek, emin misiniz? E/H").upper()
            assert cevap == "E" or "H"
        except AssertionError:
            print("Hatalı seçim")
        except:
            print("Bir hata oluştu")
        else:
            if cevap == "E":
                if path.exists("Ürünler.txt"):
                    remove("Ürünler.txt")
                    print("Dosya silindi")
                if not path.exists("Ürünler.txt"):
                    print("Dosya yoktur")
            elif cevap == "H":
                print("Geri dönülüyor")
    @abstractmethod
    def BilgiGuncelle(self):
        self.isim = input("İsim:")
        self.fiyat = float(input("Fiyat:"))
        self.marka = input("Marka:")
        self.model = input("Model:")
        self.puan = float(input("Puan:"))
    @abstractmethod
    def BilgiYaz(self):
        print(f"""
İsim:               {self.isim}
Fiyat:              {self.fiyat}
Marka:              {self.marka}
Model:              {self.model}
Puan:               {self.puan}""")
    @abstractmethod
    def BilgiSil(self):
        self.isim = ""
        self.fiyat = 0
        self.marka = ""
        self.model = ""
        self.puan = 0