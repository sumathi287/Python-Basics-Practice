# Count the number of digits in a number.
try:
    number = int(input("Enter the number to count the digit: "))
    if number < 0:
        number = -number
    count = 0
    while number > 0:
        number = int(number / 10)
        count = count + 1
    print(f"the digit presents in the number is {count}")

except ValueError:
    print("Invalid input!")
