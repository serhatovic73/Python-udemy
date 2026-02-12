# Pythonda degisken tipleri dinamik olarak belirlenir

x = 10  # x bir int 
print(type(x)) #<class 'int'>

x = "serhat" # x bir str
print(type(x)) #<class 'str'>

x = 3.4 # x bir float
print(type(x)) # <class 'float'>

#sonuc 5 olmasina ragmen hepsi farkli bir veri tipileri
a = 5 # int
b = "5" # str
c = 5.0 # float

print(type(a))
print(type(b))
print(type(c))

#degisken türlerinde dikkat edilmesi gerekenler
#bir string deger ile integer veyahut float deger toplanamaz
sayi1 = 10
sayi2 = "5"
#print(sayi1 + sayi2) #TypeError: unsupported operand type(s) for +: 'int' and 'str'

#string olmasina ragmen toplama yapmak istersek onu int degerine donusturebiliriz
print(sayi1 + int(sayi2)) #int(...) => typecast tür/tip degistirme
#yukari sayi2 yi integer degerine donusturduk ve toplama islemi sorunsuz bir sekilde calismis oldu
