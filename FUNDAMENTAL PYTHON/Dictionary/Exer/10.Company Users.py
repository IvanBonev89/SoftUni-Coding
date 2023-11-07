dictionary = {}
while True:
    command = input().split(" -> ")
    if command[0] == "End":
        break
    else:
        course_name = command[0]
        student_name = command[1]
        if course_name not in dictionary.keys():
            dictionary[course_name] = []
            dictionary[course_name].append(student_name)
        else:
            if student_name not in dictionary[course_name]:
                dictionary[course_name].append(student_name)
            else:
                continue
for course_name, student_name in dictionary.items():
    print(f"{course_name}")
    for student in student_name:
        print(f"-- {student}")
