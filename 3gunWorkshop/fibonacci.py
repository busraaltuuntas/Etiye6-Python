def fib(i: int):
    a= 1
    b =1 
    liste =[a,b]

    for x in range(1, i+1):
        a, b = b, a+b
        liste.append(b)
    return liste


print(fib(20))



