# read user input

n = int(input())

#logic


for i in range(0, n+1, 2):
    if i == 0:
        print(1)
    elif i // 2:
     print(int(pow(2,i)))

