def arrDisplay(arr):
    print("[ ",end='')
    for i in range (0,len(arr)-1):
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

def binaryToDecimal(arr):
    decimalNumber = 0
    for i in range (0,len(arr)):
        decimalNumber += arr[i] * pow(2,len(arr)-i-1)
    
    return decimalNumber

def arrayMerge(arrA,arrB):
    newArr = [0] * (len(arrA) + len(arrB))
    print(str(len(newArr)))
    a = 0
    b = 0
    for i in range (0,len(newArr)):
        if i % 2 == 0:
            newArr[i] = arrA[a]
            a+=1
        else:
            newArr[i] = arrB[b]
            b+=1

    return newArr

def rotateArr(arr):
    mode = input(" ")
    if int(mode) == 1:
        arr[0][0],arr[1][0] = arr[1][0],arr[0][0]
        arr[1][0],arr[0][1] = arr[0][1],arr[1][0]
        arr[1][0],arr[1][1] = arr[1][1],arr[1][0]
    elif int(mode) == 2:
        arr[0][0],arr[0][1] = arr[0][1],arr[0][0]
    elif int(mode) == 3:
        arr[0][0],arr[1][0] = arr[1][0],arr[0][0]
        arr[0][1],arr[1][1] = arr[1][1],arr[0][1]
    
    return arr
        
print(rotateArr([[7,4],[3,2]]))
