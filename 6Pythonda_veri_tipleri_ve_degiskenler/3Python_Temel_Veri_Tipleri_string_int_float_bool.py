"""
#String veri tipi 
ad = "Serhat"
soyad = "Kaya"

#type() fonksiyonu ile degiskenin veri tipini ogrenebiliriz
print(type(ad)) # => <class 'str'> bu sekilde cikti verir

#diger dillerde olmayip da pythonda olan bir ozellik ise 
print(ad * 2) #bunun karsiligi SerhatSerhat seklinde olacaktir diger dillerde hata verir.

#ad ve soyadi baska bir degiskene atayip terminala yazdiralim
isim = ad + " " + soyad 
print(isim)

#Pythonda java daki char yani tek karakterlik veri tipi yoktur tek karakter girildiginda string olarak dondurur.
karakter = "K"
print(type(karakter)) # <class 'str'> 

"""
#Integer (int) veri tipi
#int veri türünde herhangi bir sinirlama yoktur diger dillerde ki gibi 
# RAM inizin kaldirabildigi kadar sayi girebilirsiniz veya islem yapabilirsiniz
sayi1 = 232302302302003203231
print(sayi1) 
print(type(sayi1)) #<class 'int'>
print( sayi1 * 5) #1161511511510016016155

#FLOAT (float) veri tipi
#float veri tipi yani ondalikli sayilar 
sayi2 = 12.3432
sayi3 = -2.53

print(sayi2 + sayi3) #9.8132
print(type(sayi2)) #<class 'float'>

#BOOLEAN - bool (mantiksal degerler tutulur - True / False)
yanlis_mi  = False
dogru_mu = True

print(yanlis_mi)  #False
print(dogru_mu) #True

print(type(yanlis_mi)) #<class 'bool'>