import random

guess = 0

number = random.randint(1, 20)
print(number)

userGuess = input("guess a number: ")

while (int(userGuess )!= number):

    if (int(userGuess )> number):
        print("too high!")
        guess += 1

    elif (int(userGuess )< number):
        print("too low")
        guess += 1
    else:
        print("Correct!")
