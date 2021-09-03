#3 types of thred
# 1.Creating thread without using any class(fucntion based)
# 2.Creating thread by using extending thread class
# 3.creating thread by without extending thread class

#using function create thread

from threading import Thread
import threading
from time import sleep

def Display():
    for i in range(1,101):
        print("child thread ",i)

t1=Thread(target=Display())     #creation of thread
t2=Thread(target=Display())     #creation of thread

print(threading.active_count())
t1.start()
t2.start()

t1.join()
t2.join()

print("Sucessfully done")