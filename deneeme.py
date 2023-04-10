def topla(x,y):
    return x+y

def cikar(x,y):
    return x-y

def carp(x,y):
    return x*y

def bol(x,y):
    return x/y

def mod(x,y):
    return x%y

def hesapla():
    a=1
    while a==1:
        sayi1 = float(input("Sayı giriniz: "))
        sayi2 = float (input("Lütfen 2. sayıyı giriniz: "))
        islem = input("Lütfen işlem seçiniz  1-Toplama, 2-Çıkarma, 3-Çarpma, 4-Bölme, 5-Mod Alma : ")

        if islem == '1':
            print(topla(sayi1,sayi2))
        elif islem == '2':
            print(cikar(sayi1,sayi2))
        elif islem == '3':
            print(carp(sayi1,sayi2))
        elif islem == '4':
            print(bol(sayi1,sayi2))
        elif islem == '5':
            print(mod(sayi1,sayi2))
        else:
            print("Yanlış seçim yaptınız")
            break
hesapla()
