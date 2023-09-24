n = int(input())
count = 0
for x in range (0,26):
    for y in range (0,26):
        for z in range (0, 26):
            sum = x + y + z
            if sum == n:
                count += 1
                break

print(count)
