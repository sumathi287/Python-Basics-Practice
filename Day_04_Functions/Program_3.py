def add_numbers(a, b):
    return a + b


try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    result = add_numbers(first_number, second_number)
    print(f"The sum of the number is {result}")
except ValueError:
    print("Invalid input!!")
