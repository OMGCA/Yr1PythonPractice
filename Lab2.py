from random import *
from math import *

a = randint(1,15)
b = randint(1,15)
answer = input("What is " + str(a) + " x " + str(b) + "? ")

if int(answer) == a*b:
    print("Correct")
else:
    print("Incorrect")

userDesire = 1
while userDesire == 1:
    r = randint(1,100)
    print("I've thought of a number bewteen 1 and 100.")

    userinput = input("Take a guess: ")
    counter = 0
    while int(userinput) != r:
        if int(userinput) > r:
            print("That's too high.")
        elif int(userinput) < r:
            print("That's too low.")
        counter+=1
    
        userinput = input("Take a guess: ")

    print("That's correct, well done!")
    continueGame = input("You took " + str(counter) + " guesses. Would you like another game?")
    if continueGame == "no":
        userDesire = 0
    else:
        userDesire = 1

inputIncome = input("Input annual income: ")
income = int(inputIncome)
taxPending = 0
if income <= 11000:
    taxPending = 0
elif income > 11000 and income <= 32000:
    taxPending = (income - 11000) * 0.2
elif income > 32000 and income <= 150000:
    taxPending = 21000*0.2 + (income - 32000)*0.4
else:
    taxPending = 21000*0.2+118000*0.4+(income - 150000)*0.45

print(str(taxPending))

tmpStr = input("Side A: ")
sideA = int(tmpStr)
tmpStr = input("Side B: ")
sideB = int(tmpStr)
tmpStr = input("Side C: ")
sideC = int(tmpStr)

if sideA < sideB+sideC and sideB < sideA+sideC and sideC < sideA+sideB:
    print("Triangle valid")
    if sideA == sideB and sideB == sideC:
        print("Equilateral Triangle")
    elif sideA != sideB and sideA != sideC and sideB != sideC:
        print("Scalene Triangle")
    else:
        print("Isoceles Triangle")
else:
    print("Invalid triangle")

tmpStr = input("Enter an amount: ")
moneyValue = float(tmpStr)
remainingValue = moneyValue
smallChange = (float(moneyValue) - floor(moneyValue))*100
j = 0
count = [0,0,0,0,0,0,0,0,0,0,0,0]
while floor(remainingValue) > 0 and floor(smallChange) > 0:
    for i in [50,20,10,5,2,1]:
        count[j] = floor(remainingValue/i)
        remainingValue -= count[j] * i
        count[j+6] = floor(smallChange/i)
        smallChange -= count[j+6] * i
        j+=1

j = 0

for i in [50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]:
    if i >= 1:
        print("£" + str(i) + ": " + str(count[j]))
        
    else:
        print(str(i*100) + "p: " + str(count[j]))
        
    j+=1
