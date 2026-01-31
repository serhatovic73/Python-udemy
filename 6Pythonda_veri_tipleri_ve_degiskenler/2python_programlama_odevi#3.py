#odev: kullanicidan veri alip o verinin kac karakter oldugunu ekrana yazdiran bir fonskiyon yaziniz
karakter = input("Karakterini hesaplayacaginiz metni girin : ")
karakter_sayisi = len(karakter)
print("Verdiginiz metnin karakter sayisi : " , karakter_sayisi)

#tabi bunun kisa hali de yapilabilir 
print(len(input("Karakterini hesaplayacaginiz metni girin : ")))