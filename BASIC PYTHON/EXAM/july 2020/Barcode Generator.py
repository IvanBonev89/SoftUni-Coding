# input

num1 = int(input())
num2 = int(input())

for i in range(num1, num2 + 1):
    string = str(i)
    is_even = True
    for j in string:
        if int(j) == 0 or int(j) % 2 == 0:
            is_even = False
            break
    if is_even:
        print(string, end=' ')
