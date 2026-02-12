#int ile float toplandiginda float a donusur 
#implicit Type Casting
a = 10
b = 22.2
sonuc = a +b 
print(type(a)) #int
print(type(b)) #float
print(sonuc) 
print(type(sonuc))#float

# Explicit Type Casting

x = "123"
y = int(x) # string (x) => integer (x)
print(type(y)) #<class 'int'>
print(y + 7) #130

#simdide sayilari string olarak toplamayi ogrenelim
xx = 230
yy = "34"

print(str(xx)+yy) #23034

"""
Diger sIk kullanilan typecast donusumleri
int(x)
float(x)
str(x)
bool(x)
"""
c = "3.43"
d = float(c)
print(type(c)) #<class 'str'>
print(type(d)) #<class 'float'>

#boolen da tur donusumu
print(bool(1)) #true
print(bool(0)) #false

sayi = 5
sayi2 = bool(sayi)
print(type(sayi)) # burada int degerindedir <class 'int'>
print(type(sayi2)) # degistirdigimiz icin boolean olmustur  <class 'bool'>

