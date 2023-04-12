from ogrenciler import Ogrenci
from ogretmen import Ogretmen

listeOgrenci =[]
listeOgretmen =[]

def ogrenciKayit():
    Ogrenci.ekle(listeOgrenci)

def ogrenciOku():
    Ogrenci.oku(listeOgrenci)

def ogretmenKayit():
    Ogretmen.ekle(listeOgretmen)

def ogretmenOku():
    Ogretmen.oku(listeOgretmen)

while True:
    islem = input("Yapmak istediniz işlemi seçiniz: \n1-Öğrenci eklme  \n2-Öğretmen ekleme \n3-Öğrenci Listele \n4-Öğretmen Listele \n5-Çıkış : ")
    if islem == "1":
        ogrenciKayit()
    elif islem == "2":
        ogretmenKayit()
    elif islem == "3":
        ogrenciOku()
    elif islem == "4":
        ogretmenOku()
    elif islem == "5":
        break
print("işlem sonlandırıldı")
