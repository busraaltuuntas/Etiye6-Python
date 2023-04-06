vize = float(input("Vize notunuzu giriniz: "))
final = float(input("Final notunu giriniz: "))
ortalama = (vize * 0.4) + (final*0.6)
if vize < 100 and final< 100:

    if ortalama <50:
        print("FF")
    elif ortalama <50 and ortalama < 60:
        print("DD")
    elif ortalama < 60 and ortalama <70:
        print("CC")
    elif ortalama < 70 and ortalama <80:
        print("BB")
    elif ortalama < 80 and ortalama <101:
        print("AA")
else:
    print("Yanlış girdiniz")