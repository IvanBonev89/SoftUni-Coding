students = []
course_search = None
while True:
    student_info = input()
    if ":" not in student_info:
        course_search = student_info
        break

    name, id, course = student_info.split(":")
    students.append({"Name" : name, "Id" : id, "Course" : course})

for student in students:
    if course_search.startswith(student["Course"][0:3]):
        print(f"{student['Name']} - {student['Id']}")
