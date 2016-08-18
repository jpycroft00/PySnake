import random

class Food:
    __xRange__ = 0
    __yRange__ = 0
    x = 0
    y = 0
    def move(self):
        self.x = random.randrange(self.__xRange__)
        self.y = random.randrange(self.__yRange__)
        
    def __init__(self, xRange, yRange):
        self.__xRange__ = xRange
        self.__yRange__ = yRange
        self.move()