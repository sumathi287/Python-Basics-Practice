# Find the smallest number in a list.
var = [80, 30, 20, 55, 43]
list_length = len(var)
# The logic to rearrange the list elements in accending order
for i in range(list_length):
    count = i + 1
    for j in range(count, list_length):
        if var[i] > var[j]:
            temp = var[j]
            var[j] = var[i]
            var[i] = temp
print(f"The smallest number in the list is {var[0]}")
