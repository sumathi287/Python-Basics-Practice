number = input("Enter a number to check the number is odd or even: ")
try:
    number = int(number)
    if number % 2 == 0:
        print("The number is even!!")
    else:
        print("The number is odd!!")
except ValueError:
    print("Entered a invalid data!!!")
