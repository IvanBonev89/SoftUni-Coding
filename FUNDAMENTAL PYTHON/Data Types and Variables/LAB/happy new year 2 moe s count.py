year = int(input())
status = "unhappy"
current = 0
counter = 1
while status == "unhappy":
    current = year + 1
    current_str = str(current)
    for digit in current_str:
        status = "happy"
        if current_str.count(digit) > 1:
            status = "unhappy"
            break

    year = current


print(current)

