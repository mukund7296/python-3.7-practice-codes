a="Mukund"
b=" Biradar"
c=a+b
print(c)
print(str.__add__(a,b))
class student:

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
        s1=self.m1+other.m1
        s2=self.m2+other.m2
        s3=student(s1,s2)
        return s3

s1=student(33,44)
s2=student(77,88)

print(s1.m1)
