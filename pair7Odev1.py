sayi1 = float(input("Lütfen sayı giriniz: "))
sayi2 = float(input("Lütfen 2. sayıyı giriniz:"))

islem = input("yapmak istediniz işlemi seçiniz : (*, -,+,/) : ")

if islem == "+":
    print(sayi1 + sayi2)
elif islem == "-":
    print(sayi1 - sayi2)
elif islem == "*":
    print(sayi1 * sayi2)
elif islem == "/":
    print(sayi1 / sayi2)
else:
    print("seçim yanlıştır")