# Task 2 "Identify the Smallest":


number1 = input("Enter a Number: ")
number2 = input("Enter a 2nd Number: ")
number3 = input("Enter a Final Number: ")


if number1 < number2 and number3:
    print("The Smallest Number is", number1)
if number2 < number1 and number3:
    print("The Smallest Number is", number2)
if number3 < number1 and number2:
    print("The Smallest Number is", number3)