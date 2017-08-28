'''
Extension
'''
from random import *

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
