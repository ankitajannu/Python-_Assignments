import threading

def StraightOrder():
    for i in range(1,51,1):
        print(i)

def ReverseOrder():
    for i in range(50,1,-1):
        print(i)

def main():
    Thread1 = threading.Thread(target=StraightOrder)
    Thread2 = threading.Thread(target=ReverseOrder)

    Thread1.start()
    Thread1.join()
    
    Thread2.start()
    Thread2.join()

if __name__ == "__main__":
    main()