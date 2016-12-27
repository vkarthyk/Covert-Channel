import os
import sys
import time
import matplotlib.pyplot as plt
import mmap

latmat = []
tmat = []

if __name__ == "__main__":
    if sys.argv[1] == "recv":
        start = time.time()
        t = time.time()
        while (t - start < 10):
            l = time.time()
            a = mmap.mmap(-1, 10**9)
            for i in range(10**9):
                a[i] = i
            del a

            t1 = time.time()
            latency = t1 - l
            latmat.append(latency)
            t = time.time()
            tmat.append(t - start)
        plt.plot(tmat, latmat)
        plt.axis([0, 10, 0, max(latmat)])
        plt.show()

    elif sys.argv[1] == "send":
        bits = sys.argv[2]
        for i in range(0, len(bits)):
            if bits[i] == "0":
                time.sleep(1)
            else:
                start = time.time()
                t = time.time()
                while (t - start < 1):
                    a = mmap.mmap(-1, 10 ** 9)
                    for i in range(10 ** 9):
                        a[i] = i
                    del a
                    t = time.time()
