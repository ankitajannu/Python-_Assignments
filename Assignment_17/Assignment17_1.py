class Arithematic:
    def Add(self,No1,No2):
        Ans = 0
        Ans = No1 + No2
        return Ans

    def Sub(self,No1,No2):
        Ans = 0
        Ans = No1 - No2
        return Ans

    def Mult(self,No1,No2):
        Ans = 0
        Ans = No1 * No2
        return Ans

    def Div(self,No1,No2):
        Ans = 0
        Ans = No1 / No2
        return Ans
    
Value1 = 0
Value2 = 0
Ret = 0

Value1 = int(input("Enter first number : "))
Value2 = int(input("Enter second number : "))

obj = Arithematic()

Ret = obj.Add(Value1,Value2) 
print("Addition is : ",Ret)

Ret = obj.Sub(Value1,Value2) 
print("Subtraction is : ",Ret)

Ret = obj.Mult(Value1,Value2) 
print("Multiplication is : ",Ret)

Ret = obj.Div(Value1,Value2) 
print("Division is : ",Ret)