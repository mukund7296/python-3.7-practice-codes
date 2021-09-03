import random

l1=[]
for i in range(1,10,2):
    l1.append(i)
print(l1)


"""x=[random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9)]
d=[str(i) for i in x]
f="".join(d)
print(f)
"""


def reverse(n):
    st=""
    for i in n:
        st=i+st
    print(st)

reverse(["a","b","c","d","e"])



i=10
x=10
print(id(i))
print(id(x))
i=20
print(id(i))


l1=[1,2,3,4,5,6]

x=iter(l1)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())


"""class Student:

    def __init__(self,x):
        self.x=x


    def __iter__(self,x):
        return self.x

    def __next__(self,x):
        return self.x

ob1=Student([22,33,44,55,66,77])
print(ob1.__next__)"""



def mydec(func):
    gitt=func("Hello everyone ")
    return gitt

def title(txt):
    return txt.upper()

def name(txt):
    return txt.lower()

print(mydec(title))
print(mydec(name))


