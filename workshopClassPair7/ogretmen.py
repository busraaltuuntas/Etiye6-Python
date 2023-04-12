class Ogretmen():
   ogreciListe =[]
   def __init__(self, name, depart):
      self.name =name
      self.depart = depart

   def ekle(liste):
      ad = input("öğretmen adı: ")
      bolum= input("öğretmen bölümü: ")
      ogretmen1 =Ogretmen(ad,bolum)
      liste.append(ogretmen1)
   
   def oku(liste):
      print(f"öğretmen sayısı : {len(liste)}")
      for i in liste:
         print(f"ismi : {i.name}, departman: {i.depart}")
      
      