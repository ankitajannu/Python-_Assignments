def AreaOfCircle(radius):
    pi = 3.14159
    return pi * radius * radius

def main():
    radius = 0
    Ret = 0

    print("Enter the radius : ")
    radius = float(input())

    Ret = AreaOfCircle(radius)
    print("Area of circle is : ",Ret)

if __name__ == "__main__":
    main()