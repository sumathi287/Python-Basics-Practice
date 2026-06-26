# Create a simple Student Marks program:
def avrg_mark(mark_list, sub_count):
    count = 0
    for i in range(sub_count):
        count = count + mark_list[i]
    result = count / sub_count
    return result


def higest_mark(mark_list, sub_count):
    for i in range(sub_count):
        for j in range(i + 1, sub_count):
            if mark_list[i] > mark_list[j]:
                temp = mark_list[i]
                mark_list[i] = mark_list[j]
                mark_list[j] = temp
    return mark_list[-1]


def lowest_mark(mark_list, sub_count):
    for i in range(sub_count):
        for j in range(i + 1, sub_count):
            if mark_list[i] < mark_list[j]:
                temp = mark_list[i]
                mark_list[i] = mark_list[j]
                mark_list[j] = temp
    return mark_list[-1]


student_marks = [90, 75, 73, 85, 96]
sub_count = len(student_marks)
result = avrg_mark(student_marks, sub_count)
print(f"The average mark is {result}")
result = higest_mark(student_marks, sub_count)
print(f"The higest mark is {result}")
result = lowest_mark(student_marks, sub_count)
print(f"The lowest mark is {result}")
