from datetime import date #date fonksiyonunu import edelim
#pythonda degisken türü otomatik belirlenir

#degisken olusturduk
isim = "Hakan "
soyIsim = "Can"
yas = 22
dogumTarihi = date(2009,5,3)
anneAdi = "Cemile"
babaAdi = "Remzi"

print("Merhaba " + isim + "Hosgeldiniz! ")

print("Kimlik Verileriniz :"
       "\nAd : " + isim +
       "\nSoyad : " + soyIsim + 
        "\nYas : " + str(yas) +
        "\nDogum Tarihi : " + str(dogumTarihi) +
        "\nAnne Adi : " + anneAdi +
        "\nBaba Adi : "  + babaAdi)


