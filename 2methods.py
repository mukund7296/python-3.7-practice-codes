# 3types of methods
#1.class methods 2. instance method 3.static methods

class Student:
    school="University of pune"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):                          #instance method
        return (self.m1+self.m2+self.m3)/3  #instance method

    @classmethod                            #class method
    def info(cls):                          #class method
        return cls.school

    @staticmethod                          #static method
    def info_details():                    #static method
        print("This is static method")



s1=Student(50,60,88)
s2=Student(70,70,78)


print("*"*30)
print("Average of sutdent",s1.avg())
print(Student.info())
Student.info_details()
print("*"*30)
print("Average of sutdent",s2.avg())
print(Student.info())
Student.info_details()
print("*"*30)