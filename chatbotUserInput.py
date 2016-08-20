#gets the users name
name = input("Hello! What is your name?: ")


#ask how the user is
userAnswer = input("How are you today?: " )


#check if the answer is "good"
if userAnswer == "good":
    print("Thats good " + name)


#check if the answer is "bad"
elif userAnswer == "bad":
    print("Thats a shame " + name)


#if the answer isn't good or bad
else:
    print("Bye!" + name)


#print final message 
print("Thanks for talking with me, " + name)


