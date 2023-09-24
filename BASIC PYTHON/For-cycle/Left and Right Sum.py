# read user input

n = int(input())

# logic

sum_left = 0
sum_right = 0
for i in range(0,n):
    num = int(input())
    sum_left += num

for i in range (0,n):
    num_2 = int(input())
    sum_right += num_2

value = abs(sum_left - sum_right)
if sum_left == sum_right:
    print(f'Yes, sum = {sum_left}')
else:
    print(f'No, diff = {value}')
