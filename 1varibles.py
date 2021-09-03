#two types of varibles instance variable and static variables

class Car:
    wheel=4

    def __init__(self,mil,comp):
        self.mil=mil
        self.comp=comp

    def display(self):
        print("Millage is :",self.mil,"\nCompany name :",self.comp)

c1=Car("200 kmpl","Morris garage")

c1.display()
print("No of wheels :",c1.wheel)