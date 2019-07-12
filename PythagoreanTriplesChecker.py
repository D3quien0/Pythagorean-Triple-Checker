import math
switch = True
def pythagorean(a,b,c):
    pySideOne = a ** 2
    pySideTwo = b ** 2
    hypotenuse = c ** 2
    print()
    if pySideOne + pySideTwo == hypotenuse:
        print("The sides you have given do form a Pythagorean Triple.")
    else :
        print("The sides you have given do not form a Pythagorean Triple.")
        
while switch == True:
    print()
    integerOne = float(input("Side 1: "))
    integerTwo = float(input("Side 2: "))
    integerThree = float(input("side 3: "))
    pythagorean(integerOne,integerTwo,integerThree)
