from turtle import *
import time

#choose shape and color of turtle/line
shape("turtle")
color("red")
pensize(5)
bgcolor("black")

#draws square
'''
pensize(3)              
speed(9)

forward(100)
right(90)
Des
forward(100)
right(90)

forward(100)
right(90)

forward(100)
right(90)

#finished drawing square 
'''

'''
for i in range(20):
    forward(100)
    right(150)
'''

for i in range(100000):
    forward(100)
    right(100)
    time.sleep(5)
done()
