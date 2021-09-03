def mygen(n):
    a,b=0,1
    i=0
    while a<n:
        yield b
        a,b=b,a+b

a=mygen(8)
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())

