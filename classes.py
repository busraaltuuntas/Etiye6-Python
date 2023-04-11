#class, nesne, obje,sınıf
class Human:
    #property, attribute => özellik nitelik
    #initilaize
    def __init__(self,name, age) :
        print("Yapıcı blok çaıştı")
    #davranışlar
    #classlarda fonksiyon içine self unutmaaa!!!
    def talk(self,message):
        print(message)
    
    def walk(self):
        print(f"{self.name} is walking..")

#instance üretmek- örnek üretmek
human1 = Human("büşra", 25) #constructor => yapıcı blok 
human1.name= "Büşra"
human1.age= 25
human1.talk("Merhaba")
human1.walk()

