def ciftsayilar():
    list2 = []
    x = int(input ("Lütfen bir sayı giriniz: "))
    y= int(input("alt limit belirleryiniz"))
    if x>0:
        if y%2==0:
            for i in range(y,x,2):
                list2.append(i)
            print(list2)
        else:
            for i in range(y+1,x,2):
                list2.append(i)
            print(list2)
    else:
        print("Lütfen 0'dan büyük sayı giriniz.")
        ciftsayilar()
ciftsayilar()