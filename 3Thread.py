
import multiprocessing
import threading
from threading import Thread
from time import sleep
from multiprocessing import Process


print("current Thread :",threading.current_thread().getName())
print("current Process :",multiprocessing.current_process().name)