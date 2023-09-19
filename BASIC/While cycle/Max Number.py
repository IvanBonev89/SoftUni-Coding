import sys
max = - sys.maxsize
while True:
    number = input()
    if number == "Stop":
        break
    else:
        number_real = int(number)
        if number_real > max:
            max = number_real

print(max)

