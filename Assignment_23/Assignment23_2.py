class BankAccount:
    ROI = 10.5

    def __init__(self):
        self.Name = ""
        self.Account = 0

    def Display(self):
        print("The name of the account holder : ")
        self.Name = input()

        print("The current balance : ")
        self.Account = float(input())

    def Deposit(self):
        print("Enter the amount you want to deposit : ")
        self.Amount = float(input())

        self.Account = self.Account + self.Amount

        return self.Account

    def Withdraw(self):
        print("Enter the amount you want to withdraw : ")
        self.Amount = float(input())

        if(self.Amount <= self.Account):
            self.Account = self.Account - self.Amount
        else:
            print("Insufficient balance")

        return self.Account

    def CalculateInterset(self):
        return (self.Amount * BankAccount.ROI) / 100
  
obj1 = BankAccount()
obj1.Display()
print("The amount after deposition : ",obj1.Deposit())
print("The amount after withdraw is : ",obj1.Withdraw())
print("Interest rate is : ",obj1.CalculateInterset())

print()

obj2 = BankAccount()
obj2.Display()
print("The amount after deposition : ",obj2.Deposit())
print("The amount after withdraw is : ",obj2.Withdraw())
print("Interest rate is : ",obj2.CalculateInterset())
