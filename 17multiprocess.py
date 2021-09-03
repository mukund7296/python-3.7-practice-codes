import time
from multiprocessing import Process,Value,Array,Lock

from time import sleep

def Add_100(numbers,lock):
    for i in range(100):

        time.sleep(0.1)
        for i in range(len(numbers)):
            with lock:
                numbers[i]+=1


if __name__ == '__main__':
    lock=Lock()
    shared_array=Array("d",[0.00,100.0,200.0,300.0])
    print("Array of beigning is ",shared_array[:])

    p1=Process(target=Add_100,args=(shared_array,lock))
    p2=Process(target=Add_100,args=(shared_array,lock))

    #start process

    p1.start()
    p2.start()


    #join process
    p1.join()
    p1.join()

    print("number at the end",shared_array[:])