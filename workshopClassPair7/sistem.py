from ogrenciler import Ogrenci
from ogretmen import Ogretmen

print("Öğrenciler")
ogrenci4=Ogrenci()
ogrenci4.name=("Ezgi")
ogrenci4.number=650
ogrenci5=Ogrenci()
ogrenci5.name=("Furkan")
ogrenci5.number=150
print(ogrenci4.name,ogrenci4.number)
print(ogrenci5.name,ogrenci5.number)
print("Öğretmenler")


ogretmen1=Ogretmen()
ogretmen1.name=("Halit")
ogretmen1.depart=("Yazılım")
print(ogretmen1.name,ogretmen1.depart)
ogretmen2=Ogretmen()
ogretmen2.name=("Engin")
ogretmen2.depart=("Python")
print(ogretmen2.name,ogretmen2.depart)

