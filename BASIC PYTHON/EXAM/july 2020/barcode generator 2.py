# input

low = int(input())
high = int(input())

low_4 = low % 10
low //= 10
low_3 = low % 10
low //= 10
low_2 = low % 10
low //= 10
low_1 = low % 10
low //= 10

high_4 = high % 10
high //= 10
high_3 = high % 10
high //= 10
high_2 = high % 10
high //= 10
high_1 = high % 10
high //= 10

for i in range(low_1, high_1+1):
    if i % 2 == 0:
        continue
    for j in range(low_2 , high_2+1):
        if j % 2 == 0:
         continue
        for k in range(low_3,high_3+1):
            if k % 2 == 0:
             continue
            for l in range (low_4, high_4+1):
                if l % 2 == 0:
                    continue
                print(f"{i}{j}{k}{l}", end=' ')
