import threading
import time

exitFlag = 0


class MeinThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print "Starte" + self.name
        threadLock.acquire()
        print_time(self.name, 5, self.counter)
        threadLock.release()
        print "Verlasse " + self.name


def print_time(threadName, counter, delay):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s : %s" % (threadName, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()
thread = []

t1 = MeinThread(1, "Thread-1", 1)
t2 = MeinThread(2, "Thread-2", 2)

t1.start()
t2.start()

thread.append(t1)
thread.append(t2)

for t in thread:
    t.join()

print ("Beende Main Thread")
