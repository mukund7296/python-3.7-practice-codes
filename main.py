class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def display(self):
        print("Cpu is :",self.cpu,"\nRam is: ",self.ram)

ob1=Computer("i5",'5gb')

ob1.display()