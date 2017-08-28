from gpiozero import LED
from time import sleep

red_led = LED(4)
green_led = LED(3)

def turn_on_led(led):
	led.on()
	sleep(5)
	led.off()

print("In Python, what do you call a 'box' used to store data?")
answer = input()

if answer == "variable":
    print(" :) " * 100)
    turn_on_led(green_led)
else:
    print(" :( " * 100)
    turn_on_led(red_led)

print("Thank you for playing!")