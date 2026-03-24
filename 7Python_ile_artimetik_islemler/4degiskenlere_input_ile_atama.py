"""
#burada ismi aliriz normal bir sekilde ama sayi olunca sayilari 
toplamak yerine yan yana yazacaktir.

isim = input("lutfen adinizi giriniz : ")
metin = "Kisinin adi : " + isim

print(metin)
"""
#sayilarda int veya  float verilmelidir aksi takdirde string olarak algilar
#eger ondalikli sayi girilecekse float olarak degistirilmelidir integer veri türü
#aksi takdirde hata verecektir

sayi1 = int(input("Lütfen 1.sayiyi giriniz : "))
sayi2 = int(input("Lütfen 2.sayiyi giriniz : "))

toplam = sayi1 + sayi2

print("Toplam : " , toplam)
print(type(sayi1))
