import threading

def DisplayEven(No):
    for i in range(2,No+1,2):
        print(i)

def DisplayOdd(No):
    for i in range(1,No+1,2):
        print(i)

def main():
    Even = threading.Thread(target=DisplayEven, args=(20,))
    Odd = threading.Thread(target=DisplayOdd, args=(20,))

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()

if __name__ == "__main__":
    main()