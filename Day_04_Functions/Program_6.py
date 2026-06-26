# Calculator using functions:
def add_number(a, b):
    print(f"The sum of two number is {a+b}")


def subtract_number(a, b):
    print(f"The subtract of  two number is {a-b}")


def mul_number(a, b):
    print(f"The multiplication of two number is {a*b}")


def div_number(a, b):
    try:
        print(f"The division of two number is {a/b}")
    except ZeroDivisionError:
        print("The denominator should not be zero!!")


try:
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    add_number(first_number, second_number)
    subtract_number(first_number, second_number)
    mul_number(first_number, second_number)
    div_number(first_number, second_number)
except ValueError:
    print("Invalid input")
