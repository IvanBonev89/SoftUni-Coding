number = int(input())
list_positive = []
list_negative = []
sum= 0
for i in range(1, number+1):
    num = int(input())
    if num >= 0:
        list_positive.append(num)
    else:
        sum += num
        list_negative.append(num)

print(list_positive)
print(list_negative)
print(f"Count of positives: {len(list_positive)}")
print(f'Sum of negatives: {sum}')
