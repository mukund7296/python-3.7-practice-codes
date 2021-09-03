
class student:

    def __init__(self,a,b,c,d,e):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e

    def sort(self):
        s=self.a,self.b,self.c,self.d,self.e
        d=sorted(s)
        print("Second Heighest Numbe is : ",d[-2])


list1=student(70, 11, 20, 4, 100)
list1.sort()