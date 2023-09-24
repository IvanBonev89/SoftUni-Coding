number = int(input())
num_str = str(number)
status = False
sum = 0
for n in range (1,number+1):
    status = False
    current = str(n)
    for i in current:
        sum += int(i)
        if sum == 7 or sum == 5 or sum == 11:
            status = True

    sum = 0

    print(f"{current} -> {status}")


