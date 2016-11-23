"""
Produces load on all available CPU cores
"""

from multiprocessing import Pool
from multiprocessing import cpu_count
import psutil
from twisted.internet import task, reactor
import time
import sys

def f(x):
    for i in range(0, 22):
        x *= x

def sleep():
    print "Sending a 0"
    time.sleep(25)

def cpu_stress():
    processes = cpu_count()
    print "Sending a 1"
    pool = Pool(processes)
    pool.map(f, range(1000, 1000+processes))

if __name__ == '__main__':
    message = raw_input('Enter the message:')
    for bit in list(message):
        if bit == '1':
            cpu_stress()
            #time.sleep(30)
        elif bit == '0':
            sleep()


