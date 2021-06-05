import math


class Triangle:
    def __init__(self, point1, point2, point3):
        self.x1 = float(point1[0])
        self.y1 = float(point1[1])
        self.x2 = float(point2[0])
        self.y2 = float(point2[1])
        self.x3 = float(point3[0])
        self.y3 = float(point3[1])

    def area(self):
        Area = 0.5 * (self.x1 * (self.y2 - self.y3) + self.x2 * (self.y3 - self.y1) + self.x3 * (self.y1 - self.y2))
        return math.fabs(Area)

    def sides(self):
        side1 = math.sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2)
        side2 = math.sqrt((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2)
        side3 = math.sqrt((self.x1 - self.x3) ** 2 + (self.y1 - self.y3) ** 2)
        return [side1, side2, side3]

    def perimeter(self):
        return sum(self.sides())

    def center(self):
        xcenter = (self.x1 + self.x2 + self.x3) / 3
        ycenter = (self.y1 + self.y2 + self.y3) / 3
        return [xcenter, ycenter]

    def type(self):
        sides = sorted(self.sides())

        if sides[0]**2 + sides[1]**2 - sides[2]**2<0.01:
            return "right triangle"
        if sides[1] == sides[2] and sides[1] == sides[0]:
            return "equilateral triangle"
        if sides[1] == sides[2] or sides[0] == sides[1] or sides[0] == sides[2]:
            return "Isosceles triangle"
        return "usual triangle"




point1 = [0, 0]
point2 = [0.1, 5]
point3 = [1, 0]
my_triangle = Triangle(point1, point2, point3)
print(my_triangle.area())
print(my_triangle.sides())
print(my_triangle.perimeter())
print(my_triangle.center())
print(my_triangle.type())
