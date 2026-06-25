number = input(
    "Enter any number to check whether the number is positive or negative or zero: "
)
number = number.strip()
try:
    number = float(number)
    if number == 0:
        print('The given number is "zero"!!')
    elif number < 0:
        print('The given number is "Negative" number!!')
    else:
        print('The given number is "Positive" number!!')

except ValueError:
    print("Entered a invalid data!!End the program!!")
