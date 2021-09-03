#This is inner class or class in class

class Student:

    def __init__(self, roll, name, age, add):
        self.roll=roll       #instance varibles
        self.name=name       #instance varibles
        self.age=age        #instance varibles
        self.add=add        #instance varibles
        self.lap=self.Laptop()

    def details(self):
        print("| Roll no :",self.roll,"\t| Name :",self.name,"\t| Age :",self.age,"\t| City :",self.add,"|")

    class Laptop:
        def __init__(self):
            self.brand="Apple pro "
            self.ram="16 gb"
            self.cpu="i7 intel"

        def show(self):
            print("| Brand :",self.brand,"\t | Cpu :",self.cpu,"\t| Ram size :",self.ram,"|")


s1=Student(100,"Mukund Biradar",34,"Beijing")
s2=Student(101,"Shaurya Biradar",34,"New York")
s3=Student(102,"Soniya Jadhav",30,"Los Angles")

s1.details()
inner=Student.Laptop()
inner.show()
print()
s2.details()
inner.show()
print()
s3.details()
inner.show()
