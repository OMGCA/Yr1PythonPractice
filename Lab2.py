from random import *

a = randint(1,15)
b = randint(1,15)
answer = input("What is " + str(a) + " x " + str(b) + "? ")

if int(answer) == a*b:
    print("Correct")
else:
    print("Incorrect")

for i in [1,2,3,4,5]:
    print(i)
print ("Loop completed")

for i in range (3,15):
    print(i)



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
