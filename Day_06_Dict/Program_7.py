student_mark = {"maths": 95, "science": 96, "english": 77}
sub_total_mark = len(student_mark)
total_mark = 0
mark_list = []
# logic for calculate total mark
for i in student_mark:
    total_mark = total_mark + student_mark[i]
    mark_list.append(student_mark[i])
print(f"Total mark: {total_mark}")
# logic for calculate average mark
average_mark = total_mark / sub_total_mark
print(f"The average mark: {average_mark}")
# logic for calculate higest mark
highest_mark = mark_list[0]
for i in range(sub_total_mark):
    if highest_mark < mark_list[i]:
        highest_mark = mark_list[i]
print(f"Higest mark: {highest_mark}")
lowest_mark = mark_list[0]
for i in range(sub_total_mark):
    if lowest_mark > mark_list[i]:
        lowest_mark = mark_list[i]
print(f"Lowest_mark: {lowest_mark}")
