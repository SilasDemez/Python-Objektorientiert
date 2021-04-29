# coding=utf-8
class Bruch(object):
    def __init__(self, zaehler, nenner):
        self.zaehler = zaehler
        self.nenner = nenner

    def erweitern(self, k):
        self.nenner *= k
        self.zaehler *= k

    def kuerzen(self, k):
        self.nenner /= k
        self.zaehler /= k

    def vollstaendigkuerzen(self):
        a = self.zaehler
        b = self.nenner
        while a != b and a != 1 and b != 1:
            a, b = min(a, b), abs(a - b)
        if a == b:
            self.zaehler = self.zaehler // a
            self.nenner = self.nenner // a

    def __str__(self):
        # return str(self.zaehler) + "/" + str(self.nenner)
        if self.nenner != 1:
            return "{}/{}".format(self.zaehler, self.nenner)
        else:
            return str(self.zaehler)


b = Bruch(13, 91)
print "Kürze Bruch einfach mit 2"
#b.kuerzen(2)
print str(b.zaehler) + "/" + str(b.nenner)

print "Erweitere Bruch mit 2"
#b.erweitern(2)
print str(b.zaehler) + "/" + str(b.nenner)

print "Kürze vollständig"
b.vollstaendigkuerzen()
print  str(b)
