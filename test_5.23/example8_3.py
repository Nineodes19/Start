class Rectangle:
    def __init__(self,w,h):
        self.width = w
        self.height = h
    def getArea(self):
        return self.width * self.height
    def getPerimeter(self):
        return (self.width + self.height) * 2

t1 = Rectangle(15,6)
print("矩形t1的宽：",t1.width,",高：",t1.height)
print("矩形t1的面积：",t1.getArea())
print("矩形t1的周长：",t1.getPerimeter())

t1.width = 8
print("矩形t1新的宽：" , t1.width)

