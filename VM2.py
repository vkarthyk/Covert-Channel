import psutil
from twisted.internet import task, reactor
import time

def cpu_usage():
    if psutil.cpu_percent(interval=1) > 50:
        print '1'
    else:
        print '0'

m = task.LoopingCall(cpu_usage)
m.start(25.0) # call every second

# l.stop() will stop the looping calls
reactor.run()