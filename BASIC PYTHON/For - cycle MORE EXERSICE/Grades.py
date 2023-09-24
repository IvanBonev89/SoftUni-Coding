
students = int(input())
fail = 0
good = 0
very_good = 0
excelent = 0
total_result = 0
for student in range(1,students + 1):
    result = float(input())
    if 2.00 <= result <= 2.99:
        fail += 1
        total_result += result
    elif 3.00 <= result <= 3.99:
        good += 1
        total_result += result
    elif 4.00 <= result <= 4.99:
        very_good += 1
        total_result += result
    elif 5.00 <= result <= 6.00:
        excelent += 1
        total_result += result

avg = total_result / students
p_excelent = excelent / students * 100
p_very_good = very_good / students * 100
p_good = good / students * 100
p_fail = fail / students * 100


print(f"Top students: {p_excelent:.2f}%")
print(f"Between 4.00 and 4.99: {p_very_good:.2f}%")
print(f"Between 3.00 and 3.99: {p_good:.2f}%")
print(f"Fail: {p_fail:.2f}%")
print(f"Average: {avg:.2f}")

