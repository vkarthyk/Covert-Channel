"""
Produces load on all available CPU cores
"""

from multiprocessing import Pool
from multiprocessing import cpu_count
import psutil
from twisted.internet import task, reactor
import time

def f(x):
    for i in range(0,22):
        x *= x
    time.sleep(30)

def cpu_stress():
    processes = cpu_count()
    print 'utilizing %d cores\n' % processes

    pool = Pool(processes)
    pool.map(f, range(1000, 1000+processes))
    print "Done!"


l = task.LoopingCall(cpu_stress)
l.start(30.0) # call every second

# l.stop() will stop the looping calls
reactor.run()