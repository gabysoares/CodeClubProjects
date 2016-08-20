print("welcome to calculator!")
print()
print("1. Addition")
print("2. Multiplication")
print("3. Subtraction")
print("4. Division")
print()
choice = input("enter choice:")
print()

if choice :
    print("addition!")
    print()
    print("enter two numbers to add!")
    number1 = int(input("enter first number!:"))
    number2 = int(input("enter second number!:"))
    print()
    print("your result is:",number1+number2)


if choice == 3:
    print("subtraction!")
    print()
    print("enter two numbers to subtract!")
    number1 = int(input("enter first number!:"))
    number2 = int(input("enter second number!:"))
    print()
    print("your result is:",number1-number2)

if choice == 4:
    print("division!")
    print()
    print("enter two numbers to divide!")
    number1 = int(input("enter first number!:"))
    number2 = int(input("enter second number!:"))
    print()
    print("your result is:",number1/number2)

else:
    print("thank you for using calculator")
