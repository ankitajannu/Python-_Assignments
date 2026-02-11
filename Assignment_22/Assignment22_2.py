class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        print("Enter the radius of the circle : ")
        self.Radius = float(input())

    def CalculateArea(self):
        return Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        return 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius of the circle : ",self.Radius)
        print("Area of the circle is : ",self.CalculateArea())
        print("Circumference of the circle is : ",self.CalculateCircumference())

def main():
    obj1 = Circle()
    obj2 = Circle()
    obj3 = Circle()

    obj1.Accept()
    obj2.Accept()
    obj3.Accept()

    obj1.CalculateArea()
    obj1.CalculateCircumference()

    obj2.CalculateArea()
    obj2.CalculateCircumference()

    obj3.CalculateArea()
    obj3.CalculateCircumference()

    obj1.Display()
    obj2.Display()
    obj3.Display()

if __name__ == "__main__":
    main()