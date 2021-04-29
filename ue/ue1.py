from random import randint


class Wuerfel(object):
    def __init__(self):
        self.augen = randint(1, 6)

    def werfen(self):
        self.augen = randint(1, 6)


w = Wuerfel()
while w.augen != 6:
    w.werfen()
    print w.augen