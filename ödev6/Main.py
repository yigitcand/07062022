from Drone import Drone
mini = Drone()
mini.isim = "DJI Mini 2"
mini.fiyat = 4800
mini.marka = "DJI"
mini.model = "Mini"
mini.puan = 8.9
mini.ucus_mesafesi = "10 KM"
mini.sarj_suresi = "31 DK"
mini.kamera_cozunurlugu = '1/2.3" CMOS'

mavic_air = Drone()
mavic_air.isim = "DJI Mavic Air 2"
mavic_air.fiyat = 8500
mavic_air.marka = "DJI"
mavic_air.model = "Mavic"
mavic_air.puan = 9.8
mavic_air.ucus_mesafesi = "10 KM"
mavic_air.sarj_suresi = "34 DK"
mavic_air.kamera_cozunurlugu = '1/2" CMOS'

mini.UrunYaz()
mini.UrunListele()
# mini.UrunSil()
# mini.BilgiYaz()
# mini.BilgiGuncelle()
# mini.BilgiSil()