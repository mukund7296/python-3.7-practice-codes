import threading
from time import sleep
from threading import Thread
class Hello(Thread):
    def run(self):
        for i in range(0,500):
            print(i,"Hello")
            sleep(0.2)

class Hi(Thread):
    def run(self):
        for i in range(0,500):
            print(i,"Hi")
            sleep(0.2)

ob1=Hello()
ob2=Hi()
ob1
ob2

ob1.start()
sleep(0.2)
ob2.start()


print("Done")