def AreaOfRectangle(length,width):
    return length * width
        
def main():
    length = 0
    width = 0
    Ret = 0

    print("Enter the length of the rectangle : ")
    length = float(input())

    print("Enter the width of the rectangle : ")
    width = float(input())

    Ret = AreaOfRectangle(length,width)
    print("Area of rectangle is : ",Ret)

if __name__ == "__main__":
    main()