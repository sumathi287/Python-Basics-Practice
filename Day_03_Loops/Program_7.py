# Check whether a number is a palindrome.
try:
    number = int(input("Enter a number: "))
    temp = number
    count = 0
    count_1 = 1
    # logic to Count the number of digits in the number
    while temp > 0:
        temp = int(temp / 10)
        count = count + 1
    # Calculate the highest place value (1, 10, 100, 1000, ...)
    temp = number
    for i in range(count - 1):
        count_1 = count_1 * 10
    # Reverse the number by extracting digits and placing them in reverse positions
    count = 0
    temp_1 = 0
    while temp > 0:
        temp_1 = int((temp % 10) * count_1 + temp_1)
        temp = int(temp / 10)
        count_1 = count_1 / 10
    print(temp_1)
    if number == temp_1:
        print(f"The given number is polindrom")
    else:
        print(f"The given number is not polindrom")

except ValueError:
    print("Invalid input!!")
