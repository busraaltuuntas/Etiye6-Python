def topla(x,y):
    return x+y

def cikar(x,y):
    return x-y

def carpma(x,y):
    return x*y

def bolme(x,y):
    return x/y

def mod(x,y):
    return x%y

def hesapla():
    a=1
    while a==1: 
        sayi1 = float(input("Lütfen bir sayı giriniz: "))
        sayi2 = float(input("Lütfen ikinci sayıyı giriniz: "))
        islem = input("Lütfen yapmak istediniz işlemi seçiniz: + , - , * , / , % :")

        if islem == "+" :
            print(topla(sayi1,sayi2))
        elif islem == "-":
            print(cikar(sayi1,sayi2))
        elif islem == "*":
            print(carpma(sayi1,sayi2))
        elif islem == "/":
            print(bolme(sayi1,sayi2))
        elif islem == "%":
            print(mod(sayi1,sayi2))
        else:
            print("Yanlış tercih yaptınız")
            break

hesapla()

    

