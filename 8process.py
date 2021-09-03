#for given list of number print square and cube of every number
#list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
import multiprocessing
import threading
import time
from multiprocessing import Process
from threading import Thread
from time import sleep


def cal_square(numbers):
    for i in numbers:
        sleep(0.2)
        print(i,"Square is :",i*i)

def cal_cube(numbers):
    for i in numbers:
        sleep(0.2)
        print(i,"Cube is :",i*i*i)

Numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#no of threads creating using this method
if __name__ == '__main__':

    t1=Process(target=cal_square,args=(Numbers,))
    t2=Process(target=cal_cube,args=(Numbers,))
    start_time=time.time()
#start the thread
    t1.start()
    t2.start()

#join
    t1.join()
    t2.join()
    end_time=time.time()
    print("Total time taken ",end_time-start_time)
    print("Sucesfully done")