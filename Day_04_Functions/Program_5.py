# Create a function that accepts three numbers and returns the largest number.
def largest_num(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    third_number = int(input("Enter the third number: "))
    result = largest_num(first_number, second_number, third_number)
    print(f"The largest number is {result}")

except ValueError:
    print("Invalid input")
