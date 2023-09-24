import sys
n = int(input())
sum = 0
max_num = -sys.maxsize


for i in range(0, n):
    num = int(input())
    sum+= num
    if max_num < num:
        max_num = num


if max_num == sum - max_num:
    print('Yes')
    print(f"Sum = {max_num}")

else:
    diff = abs(max_num - (sum - max_num))
    print('No')
    print(f'Diff = {diff}')
