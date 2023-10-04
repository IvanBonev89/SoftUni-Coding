factor = int(input())
count = int(input())
counter = 0
list = []

for i in range(count+1):
    if i > 0:
        num = i * factor
        list.append(num)

print(list)
