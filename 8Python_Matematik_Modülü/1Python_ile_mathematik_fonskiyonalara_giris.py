import math
#Temel matematiksel operatorler
a = 2
b = 4

print(a + b) #toplama
print(a - b) #cikarma 
print(a * b) #carpma
print(a / b) #bolme
print(a % b) #mod kalan
print(a ** b) #us alma
print(a // b) #tam bolme

#Matematik fonskiyonlari
print("abs Fonskiyonu" ,abs(-5))      #mutlak deger 
print("round Fonksiyonu" ,round(4.5)) #yuvarlama
print("min Fonksiyonu" ,min(2,4,5))   #en kucugu alma
print("max Fonksiyonu" ,max(3,55,6))  #en buyugu alma
print("pow Fonksiyonu" ,pow(4,7))     #üs alma

#Math modulunu ekledikten sonra gelismis math fonksiyonlarini kullabiliriz
print(math.sqrt(16))     #karekok alma => 4
print(math.factorial(5)) #faktoryel hesaplama => 120
print(math.ceil(3.2))    #yukari yuvarlama => 4
print(math.floor(3.8))   #asagi yuvarlama => 3
print(math.pi)           #pi sayisini verir






print("sin",math.sin(math.radians(90))) #sin90 => 1
print("cos",math.cos(math.radians(0)))  #cos0 => 1
print("tan" ,math.tan(math.radians(45))) #tan45 =>1
