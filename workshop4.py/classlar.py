class Human:
    name ="Büşra"
    #built-in
    #constructor yapıcı blok  fonksiyon üretildiği anda çalışır.
    #initialize => init
    #yapıcı blok bir nesne üretilirken çağırıldığında 
    def __init__(self, name):
        self.name=name #değişkenatama gibi 
        print("Bir human instance'ı üretildi")
    def __str__(self):
        return f"STR Fonksiyonunda dönen değer: {self.name}"

    def talk(self, sentence):
        #self. olarak kullanırsa self sayesinde nesnenin içerisindeki diğer alanlara erişmek için
        print(f"{self.name} {sentence}")
        name= "Emre"
        print(f"{name} {sentence}")
        self.walk()
    def walk(self):
        print(f"{self.name} is walking ")
#self =>this keywordu => ilgili fonksiyonun tanımlandığı nesnenin kendisini ifade ediyor. 
#bir class için de fonksiyon kullanıyorsa bir paremetre koyuyor bu yüzden  self
#instance => örnek

human1 = Human("Arda") 
human1.name="Başak"
human1.talk("Merhaba")
human1.walk()
print(human1)

human2 = Human("Halit")
human2.name="Ece"
human2.talk("Merhaba")
human2.walk()
print(human2)

Human("Melike: ").talk("Merhaba")
#classlarda tanımlanan fonksiyonlar o nesneye ait bir alan o nesneden bir instance üretmezsek erişemeyiz

