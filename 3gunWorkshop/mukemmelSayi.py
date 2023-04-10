def mukemmelSayi():
    sayi = int(input("Sayı giriniz: "))
    toplam = 0

    for i in range (1, sayi):
        if ((sayi % i) == 0):
            toplam =toplam +i
    if (sayi == toplam):
        print("Mükemmel sayıdır")
    else:
        print("Mükemmel sayı değildir")
    
mukemmelSayi()