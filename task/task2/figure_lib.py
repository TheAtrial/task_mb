#class Figure:
#    def __init__(self):
#        self.square = 0
#    def calculateSquare(self):
#        pass

class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def calculateSquare(self):
        half_per = (self.a + self.b + self.c) / 2
        S = (half_per * (half_per-self.a) * (half_per-self.b) * (half_per-self.c))**0.5
        return S

class Circle():
    def __init__(self, r):
        self.r = r
        self.pi = 3.14
    def calculateSquare(self):
        S = self.pi * (self.r*self.r)
        return S

class DataFigure(Triangle, Circle):
    def __init__(self, a, b, c, r):
        Triangle.__init__(self, a, b, c)
        Circle.__init__(self, r)
    def check_type(self):
        try:
            if (self.a > 0 and self.b > 0 and self.c > 0 and self.r == 0):
                print(Triangle.calculateSquare(self))
                if ( self.a**2 + self.b**2 == self.c**2 or self.c**2 + self.b**2 == self.a**2 or self.a**2 + self.c**2 == self.b**2):
                    print("Triangle is right")
            elif (self.r > 0 and self.a == self.b == self.c == 0 ):
                print(Circle.calculateSquare(self))
            else:
                print("Incorrect figure")
        except TypeError:
            print("You entered incorrect data type")
        except:
            print("Undefined error")
