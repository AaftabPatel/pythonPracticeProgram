print("program for class of cube")
class cube:
    def __init__(self,side):
        self.side=side
    def total_area(self):
        return(6*self.side*self.side)
    def lateral_area(self):
        return(4*self.side*self.side)
    def volume(self):
        return(self.side*self.side*self.side)
a=int(input("Pease enter the side of cube:"))
s=cube(a)
print("total surface area of cube is:",s.total_area())
print("lateral surface area of cube is:",s.lteral_area())
print("volume of cube is:",s.volume())

