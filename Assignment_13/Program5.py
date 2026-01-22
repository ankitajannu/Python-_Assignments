def Grades(Marks):
    for i in range(Marks):
        if(Marks >= 75):
            return "Distinction"
        elif(Marks >= 60):
            return "First Class"
        elif(Marks >= 50):
            return "Second class"
        elif(Marks < 50):
            return "Fail"

def main():
    Marks = 0
    Ret = 0

    print("Enter the marks : ")
    Marks = int(input())

    Ret = Grades(Marks)
    print("The grade is : ",Ret)

if __name__ == "__main__":
    main()