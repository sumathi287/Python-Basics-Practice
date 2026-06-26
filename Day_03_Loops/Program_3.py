# Print the multiplication table of a given number.
try:
    multiplication_number = input("Enter the number to multiply: ")
    multiplication_number = int(multiplication_number)
    for i in range(1, 11):
        print(f"{i} * {multiplication_number} = {i*multiplication_number}")
except ValueError:
    print("Invalid input!")
