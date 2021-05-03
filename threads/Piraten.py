import threading
import random
import time


class Pirat(threading.Thread):
    def __init__(self, threadID, threadName):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.threadName = threadName
        self.liste = self.fillList()

    def run(self):
        while 1:
            # print "Starte" + self.name
            threadLock.acquire()
            self.fluchen()
            threadLock.release()
            # print "Verlasse " + self.name

    def fillList(self):
        f = open('swearwords.txt', 'r+')
        lines = [line for line in f.readlines()]
        f.close()
        return lines

    def fluchen(self):
        time.sleep(random.randint(0, 5))
        print self.threadName + ": " + random.choice(self.liste)


threadLock = threading.Lock()
thread = []

p1 = Pirat(1, "Pirat1")
p2 = Pirat(2, "Pirat2")

p1.start()
p2.start()

thread.append(p1)
thread.append(p2)

for t in thread:
    t.join()
