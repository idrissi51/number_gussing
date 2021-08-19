# Number Guessing

# import Module
from random import randint
lower = int(input("Enter Lower bound: "))
upper = int(input("Enter Upper bound: "))
x = randint(lower, upper)


g = 5

while g > 0:
    y = int(input("guss a number: "))
    if x == y:
        print("Wow! right guess")
        break
    else:
        print("wrong guess")
        if y < x:
            print("You guessed too small")
        else:
            print("You Guessed too high")
        print(f"You have {g-1} tries" if g >
              1 else f"The number is {x} \n Game Over")
    g -= 1
