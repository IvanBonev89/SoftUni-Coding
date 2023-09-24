# read user input

n = int(input())

# logic
sum_even = 0
sum_odd = 0
for i in range(0 , n):
    num = int(input())
    if i % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
value = abs(sum_even - sum_odd)
if sum_even == sum_odd:
  print('Yes')
  print(f"Sum = {sum_even}")

else:
    print('No')
    print(f"Diff = {value}")

