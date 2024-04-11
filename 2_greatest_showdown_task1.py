# Task 1 "Identify the Greatest":


number1 = int(input("Enter a Number: "))
number2 = int(input("Enter a 2nd Number: "))
number3 = int(input("Enter a Final Number: "))


if number1 > number2 and number1 > number3:
    print("The Largest Number is", number1)

elif number2 > number1 and number2 > number3:
    print("The Largest Number is", number2)

elif number3 > number1 and number3 > number2:
    print("The Largest Number is", number3)