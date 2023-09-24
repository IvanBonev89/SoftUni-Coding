# input

meters = 5364
days = 1
command = input()
target = 8848
#logic

while command != 'END':
    current_meters = int(input())

    if command == "Yes":
        days += 1
    else:
        days += 0
    if days > 5:
        break
    meters += current_meters
    if meters >= target:
        break
    command = input()

# output
if meters >= target:
 print(f"Goal reached for {days} days!")
else:
 print("Failed!")
 print(f"{meters}")
