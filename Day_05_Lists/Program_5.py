# Calculate the sum of all numbers in a list.
list_var = [10, 20, 30, 40, 50]
list_length = len(list_var)
count = 0
for i in range(list_length):
    count = list_var[i] + count
print(f"The sum of all numbers in list is {count}")
