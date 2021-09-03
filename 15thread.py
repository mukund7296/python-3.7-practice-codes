#import threading module
from threading import Thread

def square_num():
    for i in range(1,5):
        print(i,"^2 =",i*i)
#create main function
if __name__ == '__main__':
    threads=[]
    thread_Num=5

    #create threads
    for i in range(thread_Num):
        thread=Thread(target=square_num())
        threads.append(thread)
    #start threads
    for thread in threads:
        thread.start()
    #joinn threads
    for thread in threads:
        thread.join()
    print("End Main")
