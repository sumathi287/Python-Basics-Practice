# Count how many times a number appears in a list.
try:
    number = int(input("Enter a number to search: "))
    list_var = [1, 3, 4, 3, 1, 1]
    length_list_var = len(list_var)
    count = 0
    for i in range(length_list_var):
        if list_var[i] == number:
            count = count + 1
    print(f"The number {number} appears {count} times")
except ValueError:
    print("Invalid input!!")
