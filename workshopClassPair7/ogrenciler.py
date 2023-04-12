class Ogrenci():
   ogreciListe =[]
   def __init__(self, name, number):
      self.name =name
      self.number = number

   def ekle(liste):
      ad = input("öğrenci adı: ")
      numara= input("öğrenci numarası: ")
      ogrenci1 =Ogrenci(ad,numara)
      liste.append(ogrenci1)
   
   def oku(liste):
      print(f"Öğrenci sayısı : {len(liste)}")
      for i in liste:
         print(f"ismi : {i.name}, numarası: {i.number}")
      
      

