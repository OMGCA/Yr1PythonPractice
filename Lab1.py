name = input("What is your name? ")
print(name)
age = input("What is your age in years? ")
print(age)
height = input("How tall are you in meters? ")
print(height)
ageInSecond = int(age) * 24 * 365 * 3600
heightInFeet = float(height) * 3.208
print("Hi " + name + ", you are " + str(ageInSecond) + " seconds old and " + str(heightInFeet) + " feet tall!" )
