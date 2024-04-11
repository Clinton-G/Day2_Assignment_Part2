# Task 1 "Leap Year Checker":


leap = int(input('Enter the Current Year '))


if leap % 400 == 0:
    print("It's a Leap Year!" )


elif leap % 4 == 0 and leap % 100 != 0:
    print("It's a Leap Year!" )

else:
    print("It's Not a Leap Year ")