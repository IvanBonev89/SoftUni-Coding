n = int(input())
counter = 0
total = 0
for i in range(n):
    num = int(input())
    total += num
    counter += 1
avg = total / counter
print(f'{avg:.2f}')
