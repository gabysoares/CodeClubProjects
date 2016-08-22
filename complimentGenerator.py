from random import *

'''
Exercise on to introduce lists and 
how to acess each element.
'''

#create list of names
names = ['Gaby', 'Craig', 'Angelo']

#to get first name
print(names[0])

#to get second name
print(names[1])

#to get third name
print(names[2])

print()

#####################################

'''
Using lists and the choice() function to 
create a random compliment generator.
'''

#prints welcome message
print("--------------------")
print("Compliment Generator")
print("--------------------")

#gets the users name 
name = input("What is your name?: ")

#list of different compliments, separated by commas
compliments = [ "Great job on that thing you did. Really super",
                "You have really really nice programming skills" ,
                "You make an excellent human",
                "You are pretty cool"
              ]

#print a random item in the 'compliments' list
print(choice(compliments), name)

#####################################

'''
Extension
'''

#prints welcome message
print("--------------------")
print("Compliment Generator")
print("--------------------")

#gets the users name 
name = input("What is your name?: ")

#list of different adjective and hobbies, separated by commas
adjectives = ["amazing" , "ok" , "excellent"]
hobbies = ["singing" , "running" , "swimming"]

#prints message and the users name from input()
print("Here is your compliment" , name , ":")

#prints name and random items from the adjectives and hobbies list
print(name , "you are" , choice(adjectives) , "at" , choice(hobbies))
 
#####################################

#can add while loop to keep program running until user selected to quit

#the program loops as long as this variable is 'True'
running = True

#prints welcome message
print("--------------------")
print("Compliment Generator")
print("--------------------")

#gets the users name 
name = input("What is your name?: ")

#list of different adjective and hobbies, separated by commas
adjectives = [ "amazing" , "ok" , "excellent" ]
hobbies = [ "singing" , "running" , "swimming" ]

#prints menu for user to get compliment or quit the program
print('''
Menu
  1 = get compliment
  2 = quit
''')

#keeps program running until user selects '2' to quit
while running == True:

	#gets user input
	menuChoice = input()

	#'1' for a compliment
	if menuChoice == '1':

		#prints message and users name from input()
		print( "Here is your compliment" , name , ":" )

		#get a random item from both lists, and create compliment
		print( name , "you are" , choice(adjectives) , "at" , choice(hobbies) )
		print()
		print("Enter 1 to get another compliment or 2 to quit")
		print()

	#'2' to quit
	elif menuChoice == '2':
		print("Thank you for playing Compliment Generator")
		#this causes while loop to end
		running = False

	#if user enters anything other than '1' or '2' for the menu choice.
	else:
		print("Please choose a valid option!")



