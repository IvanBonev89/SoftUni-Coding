number = int(input())
list = []
filtred = []
for i in range(1, number + 1):
    n = int(input())
    list.append(n)

command = input()
if command == 'even':
    for i in list:
        if i % 2 == 0:
            filtred.append(i)
elif command == 'odd':
    for i in list:
        if i % 2!= 0:
            filtred.append(i)
elif command == 'positive':
    for i in list:
        if i >= 0:
            filtred.append(i)
elif command == 'negative':
    for i in list:
        if i < 0:
            filtred.append(i)

print(filtred)
