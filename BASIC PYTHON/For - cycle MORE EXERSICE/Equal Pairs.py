n = int(input())
v = None
sum_1 = list()

sum = list()
for i in range(1,n+1):
    a = int(input())
    b = int(input())
    s = a+b
    sum.append(s)
for g in range(len(sum)-1):
    v = abs(sum[g+1] - sum[g])
    sum_1.append(v)
if v == 0 or n == 1:
    print(f'Yes, value={sum[0]}')
else:
    print(f'No, maxdiff={abs(max(sum_1))}')

