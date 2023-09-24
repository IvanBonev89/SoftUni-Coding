counter = int(input())

prew_sum = int(input()) + int(input())

max_diff = 0

for i in range (counter - 1):
    current_sum = int(input()) + int(input())
    curr_deff = abs(prew_sum - current_sum)
    if max_diff < curr_deff:
        max_diff = curr_deff
    prew_sum = current_sum

if max_diff == 0:
    print(f'Yes, value={prew_sum}')
else:
    print(f'No, maxdiff={max_diff}')

