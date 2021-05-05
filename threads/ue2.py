import threading


class Paintbox(threading.Thread):
    def __init__(self, maxStifte):
        self.maxStifte = maxStifte;

    def aquirePens(self, numberOfPens):
        threadLock.acquire()
        if numberOfPens > self.maxStifte:
            self.maxStifte -= numberOfPens

            threadLock.release()



    def releasePens(self, numberOfPens):
        print "test"


class Child(threading.Thread):
    def __init__(self, name, malkasten):
        self.name = name
        self.malkasten = malkasten


threadLock = threading.Lock()
