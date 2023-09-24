n = int(input())

for i in range(1111, 9999+1):
    string = str(i)
    is_special = True
    for j in string:
        if int(j) == 0 or n % int(j) != 0:
            is_special = False
            break
    if is_special:
        print(string, end=" ")
