class Zaehler(object):
    i = 0

    def __init__(self, obergrenze):
        while (1):
            if self.i == obergrenze:
                self.i = 0
            print self.i
            self.i += 1


z = Zaehler(60)
