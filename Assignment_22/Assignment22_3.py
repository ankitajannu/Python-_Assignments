class Arithematic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        print("Enter first number : ")
        self.Value1 = int(input())

        print("Enter second number : ")
        self.Value2 = int(input())

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2
        
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        try:
            Ans = self.Value1 / self.Value2 
            return Ans
        except(ZeroDivisionError):
            print("Division by zero is not allowed")
            return

def main():
    obj1 = Arithematic()
    
    obj1.Accept()

    print("Addition is : ", obj1.Addition())
    print("Subtraction is : ", obj1.Subtraction())
    print("Multiplication is : ", obj1.Multiplication())

    Ret = obj1.Division()
    if Ret != None:
        print("Division is : ", Ret)

    print()

    obj2 = Arithematic()

    obj2.Accept()

    print("Addition is : ", obj2.Addition())
    print("Subtraction is : ", obj2.Subtraction())
    print("Multiplication is : ", obj2.Multiplication())

    Ret = obj2.Division()
    if Ret != None:
        print("Division is : ", Ret)

if __name__ == "__main__":
    main()