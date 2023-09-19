min = int(input())

while True:
    num = input()
    if num == 'Stop':
        break
    num_real = int(num)
    if num_real < min:
        min = num_real
print(min)

