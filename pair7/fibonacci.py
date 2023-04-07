#yönteme 1

def fib(i: int):
    a= 1
    b =1 
    liste =[a,b]

    for x in range(1, i+1):
        a, b = b, a+b
        liste.append(b)
    return liste


print(fib(20))

#yöntem2 
sayi1 = 0
sayi2 = 1
l= [1]
for i in range(20):
    sayi2= sayi1+ sayi2
    sayi1= sayi2 - sayi1
    l.append(sayi2)
print(l)


