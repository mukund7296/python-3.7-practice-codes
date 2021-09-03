mytuple = ("apple", "banana", "cherry")
myit=iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


x={i:i*i for i in range(1,11)}
print(x)