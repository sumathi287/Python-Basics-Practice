#arithmetic operations
import sys

print("Welcome to arithmetic program")
try:
    number1 = input("enter the 1st number to perform arithmetic operations")
    number1 = int(number1)
    number2 = input("enter the 2nd number to perform arithmetic operations")
    number2 = int(number2)
except ValueError:
    print("Entered a wrong charecter instead of enter the number!!\nEnd the program!!")
    sys.exit()

print(f"the addition of two given numbers is {number1 + number2}")
print(f"the subraction of two given number is {number1 - number2}")
print(f"the multiplication of two given number is {number1 * number2}")
print(f"the devision of two given number is {number1 / number2}")
