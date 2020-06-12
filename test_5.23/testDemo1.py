class Circle:
    def __init__(self,r):
        self.radius = r
    def getArea(self):
        return self.radius * self.radius * 3.14
    def getPerimeter(self):
        return self.radius * 3.14 * 2

if __name__ == '__main__':

    for i in range(1,10):
        p = Circle(i)
        print("半径为",i,"的圆，面积：",p.getArea(),"周长：",p.getPerimeter())