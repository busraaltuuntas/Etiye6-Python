bigestValue = 0
secondBigestValue =0
for i in range (10):
    sayi = int(input(f"{i+1}. sayıyı giriniz: "))
    if sayi > bigestValue:
        secondBigestValue = bigestValue
        bigestValue =sayi
        

print(f"Girdiğiniz sayılar arasından en büyük olanı: {bigestValue}")
print(f"Girdiğiniz sayılar arasından 2. en büyük olanı: {secondBigestValue}")



sayilar =[]
for i in range (3):
    sayilar.append(int(input(f"{i+1}. sayı giriniz: ")))
ayilar.sort(reverse=True)
print(sayilar)
enBuyukN= int(input("Sayılar arasından en büyük kaçıncı istiyorsun? : "))
print(sayilar[enBuyukN-1])

forRange = int(input("Üst limit giriniz: "))

for i in range(forRange + 1):
    if i % 2 == 0:
        print(i)

for i in range(0,forRange+1, 2):
    print(i)

forRangeMin = int(input("Döngünün alt limitini belirleyiniz: "))
forRangeMax = int(input("Döngünün üst limitini belirleyiniz: "))
for i in range(forRangeMin, forRangeMax+1):
    if i % 2 == 0:
        print(i)