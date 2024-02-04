number_divisor = int(input())
limit_number = int(input())
x = 0

for i in range(limit_number, number_divisor, -1):
    if i % number_divisor == 0 and i > 0:
        x = i
        break
    else:
        continue

print(x)
