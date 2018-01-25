class Shape():
    def __init__(self,type):
         self.type = type

    def draw(self):
        print("Drawing from parent class")


class Rectangle(Shape):
    def __init__(self,typ,len,bre):
        super().__init__(typ)
        self.len = len
        self.bre = bre
        self.area = 0

    def draw(self):
        print("this is a rect")



    def calc_area(self):
        self.area = self.len * self.bre

    def __str__(self):
        return "the area of %s is: " %(self.type) + str(self.area) + "\n" + "the type of the shape is: "   + self.type


class Square(Rectangle):
    def draw(self):
        print("this is a square")


# r = Rectangle("rectangle",2,2)
# r.calc_area()
# print(r.__str__())

s = Square("square",1,1)
s.calc_area()
print(s.__str__())

s.draw()