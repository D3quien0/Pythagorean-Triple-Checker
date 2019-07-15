import math

def pythagorean(a,b,c):
    pySideOne = a ** 2
    pySideTwo = b ** 2
    hypotenuse = c ** 2
    print()
    if pySideOne + pySideTwo == hypotenuse:
        print("The sides you have given do form a Pythagorean Triple.")
    else :
        print("The sides you have given do not form a Pythagorean Triple.")

print()
while True:
    try:
        integerOne = float(input("Side 1: "))
        break
    except ValueError:
        print("invalid entry ")
        continue
while True:    
    try:
        integerTwo = float(input("side 2: "))
        break
    except ValueError:
        print("invalid entry")
        continue
while True:    
    try:
        integerThree = float(input("side 3: "))
        break
    except ValueError:
        print("invalid entry")
        continue
pythagorean(integerOne,integerTwo,integerThree)
