number = int(input())
total_grade = 0
float_total_grade = 0
dictionary = {}
for i in range(1,number+1):
    name = input()
    grade = float(input())
    if name not in dictionary:
        dictionary[name] = []
        dictionary[name].append(grade)
    else:
        dictionary[name].append(grade)


for name, grade in dictionary.items():
    for i in grade:
        total_grade += i
        float_total_grade = float(total_grade)
    avarage_grade = float_total_grade / len(dictionary[name])
    total_grade = 0
    float_total_grade = 0
    if avarage_grade >= 4.50:
        print(f"{name} -> {avarage_grade:.2f}")
    else:
        continue
