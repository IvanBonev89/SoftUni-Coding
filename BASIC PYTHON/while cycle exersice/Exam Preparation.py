fail_counter = int(input())
name = input()
graduate = int(input())
fail_graduate = 0
if graduate <= 4:
    fail_graduate += 1
total_graduate = graduate
counter_graduate = 1
last_name = ""
while True:
    name = input()
    if name == 'Enough':
        avg = total_graduate / counter_graduate
        print(f"Average score: {avg:.2f}")
        print(f"Number of problems: {counter_graduate}")
        print(f"Last problem: {last_name}")
        break
    graduate = int(input())
    total_graduate += graduate
    counter_graduate += 1
    last_name = name
    if graduate <= 4.00:
        fail_graduate += 1
    if fail_graduate >= fail_counter:
        print(f"You need a break, {fail_graduate} poor grades.")
        break

    else:
        continue
