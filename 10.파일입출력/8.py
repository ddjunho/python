import math
class Circle:
    r, area = 0, 0.0
    def __init__(self, x=0):
        self.r= x
        self.area = self.calcArea()
    def setR(self, x=0):
        self.r = x
    def calcArea(self):
        return math.pow(self.r, 2) * math.pi
    def print(self):
        print("반지름 %d 의 원의 넓이는 %.2f" % (self.r, self.area))

class Cylinder(Circle):
    length, volume = 0, 0.0
    def __init__(self, r=0, l=0):
        self.setR(r)
        self.setLength(l)
        self.volume = self.calcVolume()
    def setLength(self, x=0):
        self.length = x
    def calcVolume(self):
        return self.calcArea() * self.length
    def print(self):
        print("반지름 %d 의 실린더 부피는 %.2f" % (self.r, self.volume))

myCylinder1 = Cylinder()
myCylinder1.calcVolume()
myCylinder1.print()
myCylinder2 = Cylinder(3, 2)
myCylinder2.calcVolume()
myCylinder2.print()
