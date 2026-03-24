islem = input("islem türünü seciniz (+,-,*,/) : ")
sayi1 = float(input("birinci sayiyi giriniz :"))
sayi2 = float(input("ikinci sayiyi girinz : "))



if islem == "+":
     print("Sonuc : " , sayi1 + sayi2)

if islem == "-":
     print("Sonuc : " , sayi1 - sayi2)

if islem == "*":
     print("Sonuc : " , sayi1 * sayi2)

elif islem == "/":
    if sayi2 != 0:
     print("Sonuc : " , sayi1 / sayi2)
    else:     
     print("Sayi sifira bolunemez!")

if islem == "%":
     print("Sonuc : ", sayi1 % sayi2)
     
if islem == "**":
     print("Sonuc : ", sayi1 ** sayi2)
     

if islem == "//":
     print("Sonuc : ", sayi1 // sayi2)
     