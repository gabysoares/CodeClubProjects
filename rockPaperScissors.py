#1. Rock, 2. Paper, 3. Scissors

answer = 1

while True:
	user_option = input("1. Rock, 2.paper, 3. scissors?\n")

	if int(user_option) == answer:
		print("Correct")
		exit()

	else:
		print("Incorrect, try again")


if what you are writing is smaller than a specific size then you are gauranteed 