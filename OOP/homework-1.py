import math

class Point :        
    def __init__(self, x:float, y:float) :
        self.x = x
        self.y = y
        
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
        

class Line :
    def __init__(self, coord1: Point, coord2 : Point) :
        self.first_point = coord1
        self.second_point = coord2
        
    def distance(self) :
        return math.sqrt((self.second_point.x - self.first_point.x)**2 + (self.second_point.y - self.first_point.y)**2)
    
    def slope(self) :
        return (self.second_point.y - self.first_point.y) / (self.second_point.x - self.first_point.x)

class Cylinder :
    def __init__(self, height = 1, radius = 1) :
        self.height = height
        self.radius = radius
    
    def volume (self) :
        return self.radius**2 * math.pi * self.height
    
    def area (self) :
        return (2 * math.pi * self.radius**2) + (2 * math.pi * self.radius**2)

l1 = Line( Point(*(3,2)), Point(8,10) )

print(l1.distance())
print(l1.slope())

# c1 = Cylinder(5, 2)
# print(c1.area())