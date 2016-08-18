from bdb import Breakpoint
class Snake:
    SegPosX = list()
    SegPosY = list()
    length = 1
    def __init__(self,xRange,yRange):
        self.SegPosX.append(int(xRange/2))
        self.SegPosY.append(int(yRange/2))
    
    def grow(self, GrowthFactor = 1, direction = "right"):
        i=0
        while i < GrowthFactor:
            self.SegPosX.append(self.SegPosX[(self.length - 1)])
            self.SegPosY.append(self.SegPosY[(self.length - 1)])
            self.Move(direction)
            i += 1
        self.length += GrowthFactor
        
    def die(self):
        for i in self.length:
            self.SegPosX.pop()
            self.SegPosY.pop()
        self.length = 1
        
    def Move(self,direction):
        if direction == "up":
            i = len(self.SegPosX) - 1
            while i >= 0:
                if i > 0:
                    self.SegPosY[i] = self.SegPosY[i -1]
                    self.SegPosX[i] = self.SegPosX[i -1]
                else:
                    self.SegPosX[i] = self.SegPosX[i]
                    self.SegPosY[i] = self.SegPosY[i] -1
                i -= 1

        elif direction == "down":
            i = len(self.SegPosX) - 1
            while i >= 0:
                if i > 0:
                    self.SegPosY[i] = self.SegPosY[i -1]
                    self.SegPosX[i] = self.SegPosX[i -1]
                else:
                    self.SegPosX[i] = self.SegPosX[i]
                    self.SegPosY[i] = self.SegPosY[i] +1
                i -= 1
                
        elif direction == "left":
            i = len(self.SegPosX) - 1
            while i >= 0:
                if i > 0:
                    self.SegPosY[i] = self.SegPosY[i -1]
                    self.SegPosX[i] = self.SegPosX[i -1]
                else:
                    self.SegPosX[i] = self.SegPosX[i] -1
                    self.SegPosY[i] = self.SegPosY[i]
                i -= 1
                
        elif direction == "right":
            i = len(self.SegPosX) - 1
            while i >= 0:
                if i > 0:
                    self.SegPosY[i] = self.SegPosY[i -1]
                    self.SegPosX[i] = self.SegPosX[i -1]
                else:
                    self.SegPosX[i] = self.SegPosX[i] +1
                    self.SegPosY[i] = self.SegPosY[i]
                i -= 1
        else:
            Breakpoint