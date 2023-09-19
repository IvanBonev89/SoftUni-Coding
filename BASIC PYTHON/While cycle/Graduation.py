name = input()
fail = 0
classes = 0
total = 0
finish = 0
while True:
    graduate = float(input())
    if graduate < 4.00:
        fail += 1
        if fail > 1:
         finish = classes + fail - 1
         print(f"{name} has been excluded at {finish} grade")
         break
    else:
        classes += 1
        total += graduate
        if classes >= 12:
            break

if fail <= 1:
 avg = total / classes
 print(f'{name} graduated. Average grade: {avg:.2f}')
