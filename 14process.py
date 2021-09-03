from multiprocessing import Process
import os

def Squarenum():
    for i in range(100):
        print(i*i)


process=[]
num_process=os.cpu_count()

#create process
for i in range(num_process):
    p=Process(target=Squarenum())
    process.append(p)


#start
for p in process:
    p.start()

#join
for p in process:
    p.join()

