class Pycharm:
    def execute(self):
        print("Cpp program")
        print("C program")
        print("Linux program")
        print("Windows program")

class Visual:
    def execute(self):
        print("Cpp program")
        print("C program")
        print("Linux program")
        print("Windows program")
        print("Python program")
        print("R Language program")
        print("Hadoop program")
        print("Tableau program")

class Laptop:

    def code(self,ide):
        ide.execute()

ide=Visual()
lap1=Laptop()
lap1.code(ide)