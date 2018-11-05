from math import *

def xtMedianCalc(arr):
    try:
        arr.sort()
        return arr[floor(len(arr)/2)]
    except Exception:
        print("Array may need double check")

def removeAllZeros(arr):
    while True:
        try:
            arr.remove(0)
        except ValueError:
            break
    return arr

def recursionFactorial(i):
    if i == 0:
        return 1
    else:
        return i*recursionFactorial(i-1)
    
def recursionFibonacci(i):
    if i == 1:
        return 1
    else:
        return recursionFibonacci(i-1) + recursionFactorial(i-2)