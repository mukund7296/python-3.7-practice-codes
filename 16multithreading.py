import threading
from threading import Thread,Lock
from time import sleep
import time
database_value=0

def increase(lock):
    global database_value
    with lock:
        local_copy=database_value
        local_copy+=1
        time.sleep(0.2)
        database_value=local_copy




if __name__ == '__main__':
    lock=Lock()
    print("start Value ",database_value)

    thread1=Thread(target=increase,args=(lock,))
    thread2=Thread(target=increase,args=(lock,))
    thread3=Thread(target=increase,args=(lock,))

    print("Total thread =",threading.active_count())
    thread1.start()
    thread2.start()
    thread3.start()
    print("Total thread =",threading.active_count())

    thread1.join()
    thread2.join()
    thread3.join()

    print("End value",database_value)
