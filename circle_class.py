print("program for class of circle")
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return(3.14*self.radius*self.radius)
    def circumferance(self):
        return(2*3.14*self.radius)
c1=circle(10)
c=int(input("Pease enter the radius of second circle:"))
c2=circle(c)
print("area of circle 1 is:",c1.area())
print("area of circle 2 is:",c2.area())
print("circumferance of circle 1 is:",c1.circumferance())
print("circumferance of circle 2 is:",c2.circumferance())

