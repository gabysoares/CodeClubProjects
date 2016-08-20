print('======= WELCOME TO GABY''S QUIZSHOW! =======')
score = 0


#ask first question
print("What city is this years Olympics in?")
answer = input()

if answer == "Rio" or answer == "rio":
    print("Correct!")
    score += 1
    print("Your current score is:", score)

else:
    print("Your current score is:", score)
 
print()

#ask second question
print("What is the national bird of New Zealand?")
answer = input()

if answer == "kiwi" or answer == "Kiwi":
    print("Correct!")
    score += 1
    print("Your current score is:", score)

else:
    print("Your current score is:", score)
print()

#add more questions here


#print final score and goodbye message
print()
print("Thank you for playing! Your final score was", score)


