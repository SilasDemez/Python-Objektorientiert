class Kreis(object):
    def __init__(self, radius, posX, posY, color):
        self.__radius = radius
        self.__posX = posX
        self.__posY = posY
        self.__color = color

    def setX(self, x):
        self.__posX = x

    def setX(self, y):
        self.__posY = y