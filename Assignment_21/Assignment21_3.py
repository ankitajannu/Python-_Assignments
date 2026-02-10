import threading

def Increment(Counter,LockObj,NoOfTimes):
    for i in range(NoOfTimes):
        LockObj.acquire()
        Counter[0] = Counter[0] + 1
        LockObj.release()

def main():
    ThreadCount = 3
    IncrementTime = 1000

    Counter = [0]
    LockObj = threading.Lock()

    ThreadList = []

    for i in range(ThreadCount):
        Thread = threading.Thread(target=Increment,args=(Counter,LockObj,IncrementTime)) 
        ThreadList.append(Thread)
        Thread.start()

    for Thread in ThreadList:
        Thread.join()   

    print("Final value of the counter is : ",Counter[0])

if __name__ == "__main__":
    main()