import time
from threading import Thread
import threading
from time import sleep

def square():
    for i in range(101):
        print(i,"Square is",i*i)
        sleep(0.2)

def cube():
    for i in range(101):
        print(i,"cube is",i*i*i)
        sleep(0.2)

t1=Thread(target=square)
t2=Thread(target=cube)
start_time=time.time()
t1.start()
sleep(0.2)
t2.start()
print("Total thread",threading.active_count())
t1.join()
t2.join()
end_time=time.time()
print("Total time taken :",end_time-start_time)
print("Sucessfully done")
