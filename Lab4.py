def arrDisplay(arr):
    print("[ ",end='')
    for i in range (0,len(arr)-2):
        print(str(arr[i]) + " , ",end='')
    print(str(arr[len(arr)-1]) + " ]")

def insertAvg():
    arr = [0] * 10
    newArr = [0] * 19
    print("Please input 10 numbers: ")
    for i in range (0,10):
        arr[i] = int(input(" "))
        newArr[i*2] = arr[i]
    
    print("Your 10 numbers are ",end='')
    arrDisplay(arr)
    

    for i in range (0,9):
        newArr[i*2+1] = (arr[i] + arr[i+1]) / 2
    arrDisplay(newArr)

insertAvg()