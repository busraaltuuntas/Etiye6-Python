print("Merhaba Etiya")
print("Hoş geldiniz")

#yorum satırı

#değişkenler start
# metinsel,numeril, obje => çift tırnak ilgili verinin metinsel değer olduğunu belirtir

#string
text = "Merhaba "

print(text)
print(text)
print(text)
text = "Selam"
print(text)
print(text)

studentCount = "45" #string
print(studentCount)
studentCount =45 #int => integer
print(studentCount + 5)

aweragePoint = 25.5 #double,flooat, decimal
print(aweragePoint + 5)

isVerified= True #bool, boolean => true or false
print(isVerified)

print(type(text))
print(type(studentCount))
print(type(aweragePoint))
print(type(isVerified))

#değişkenler end

#operatörler start
number= 10
#matematiksel operatörler 
print(10 + 10)
print(number + number)

print(number - 5)

print(number / 2)

print(number * 5)

#mod operatörü => %  sol taraftaki değerin sağ taraftaki değere bölümünden kalan sonuç
print(number % 3)

print(number + ((10 -number) * (5/10)))

#mantıksal operatörler mantıksal operatörlerin geriye dönüş tipi booleandır bu yüzden true yada false döner
print(number == 10 ) # == eşitlik kontrol eder
print(number != 10)  # != eşit değildir kontrol eder

print(number > 10) # > büyüklük kontrolü
print(number >= 10)# >= büyük eşittir kontrolü

print(number < 10) # < küçüklük kontrolü
print(number <= 10)# <= küçük eşittir kontrolü

#operatörler end
print("**************")
#diziler -listeler start
sayilar = [100, 200, 300, 400, 500, "Merhaba", 15.5, True] #listedeki tüm elemnaların veri tipi aynı olmak zorunda değildir
#index => 0 başlangıç değeri -1 son indeksi temsil eder
print(sayilar[0])
print(sayilar[5])

sayilar.append(600)#listenin sonuna eleman ekleme 

sayilar.append(100)
print(sayilar)
sayilar.pop()#indeks belirtmezsen son elemanı indeks belirtirsen o elemanı siler
print(sayilar)
sayilar.remove(100) #değeri 100 olan ilk elemanı silicek 2. değer yerinde kalıyor
print(sayilar)
sayilaraEkleme = [700, 800, 900]
sayilar.extend(sayilaraEkleme)#liste eklemesi yapıyor yani 2 liste birleştirmek 
print(sayilar)
sayilar.clear() #dizinin içini boşaltan fonksiyon
print(sayilar)

#diziler end

#string interpolation start
hello = "Merhaba"
userName = "Büşra"
totalText = hello + " " + userName
print("Merhaba" + "Büşra")
print(hello + " " +userName)
print(totalText)

totalText = "{message} {name}".format(message = "Merhaba", name ="Emre") #metin olmaksızın ekleyyebiliyor
print(totalText)
totalText1 = "{message} {name}".format(message = "Merhaba", name =5)
print(totalText1)

#f- string
totalText2 = f"Hoşgeldiniz {userName}"
print(totalText2)
#string interpolation end

#karar yapıları start
ortalamaNot = input("Lütfen ortalamanızı giriniz: ")

#type conversion start(metin dönüştürme)
ortalamaNotAsInteger = int(ortalamaNot)

#type conversion end

#if else blokları
#4 satır => 1 tab/indent
if ortalamaNotAsInteger > 80:
    print("Bravo")
    
#else if =>elif
elif ortalamaNotAsInteger >60:
    print("Ortalama")
elif ortalamaNotAsInteger > 50:
    print("Normal")
else:
    print("Malesef")
    print("Kaldınız")
print("if bloğundan bağımsız kısım")


vize = int(input("Vize notunuzu giriniz: "))
final = int(input("Final notunu giriniz: "))
ortalama = (vize * 0.4) + (final*0.6)
# eğer final 40'dan küçükse kullanıcı kaldı
# eğer ortalama 50'den küçükse kullanıcı kaldı
# eğer vize finalin 2 katı ise kullanıcı kaldı
# bunun dışındaki tüm durumlarda kullanıcı geçti yazdırmak istiyoruz.

if final <40:
    print("Kaldınız")
elif ortalama < 50:
    print("Kaldınız")
elif (vize*2) == final:
    print("Kaldınız")
else:
    ("Geçtiniz")

#karar yapıları end
