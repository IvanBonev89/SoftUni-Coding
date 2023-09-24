low = int(input())
high = int(input())
magic_num = int(input())
count = 0
is_found = False
for i in range (low, high+1):
    if is_found:
        break
    for j in range (low , high+1):
        count += 1
        if is_found:
            break
        if i + j == magic_num:
            print(f"Combination N:{count} ({i} + {j} = {magic_num})")
            is_found = True
            break
if not is_found:
 print(f"{count} combinations - neither equals {magic_num}")
