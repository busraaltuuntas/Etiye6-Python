#classes.py içindeki Human'ı kullan
#import classes => tüm classes modülünü import eder
from classes import Human # => classes modülününden Humanı import eder
import random #pythonda ki hazır modül

#alias => takma ad
#from classes import Human as Insan
#import classesas Classlarım

human1 =Human("Büşra",25)
human1.talk("Selam")
print(random.random())