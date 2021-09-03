import threading
from threading import Thread

class Moriss_garage(Thread):
    for i in range(1,101):
        print("child thread")

t1=Moriss_garage()
t1.start()
for i in range(101):
    print("main thread")
t1.join()