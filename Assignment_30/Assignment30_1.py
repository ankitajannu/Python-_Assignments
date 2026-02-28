import os

def main():
    try:
        FileName = input("Enter the name of file : ")
        
        fobj = open(FileName,"r")
            
        Count = 0

        for lines in fobj:
            Count = Count + 1

        print("Total number of lines are : ",Count)

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of application")

if __name__ == "__main__":
    main()