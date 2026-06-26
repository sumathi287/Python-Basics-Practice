# Create a function that accepts two numbers and prints their sum.
def odd_even(number):
    number = number % 2
    return number


try:
    number = int(input("Enter a number: "))
    result = odd_even(number)
    if result == 0:
        print(f"The {number} is even!!")
    else:
        print(f"The {number} is odd!!")
except ValueError:
    print("Invalid input!!")
