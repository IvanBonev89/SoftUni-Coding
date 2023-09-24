# read user input
from math import pow
n = int(input())

#logic

for i in range(0, n+1):
    if i == 0:
        print(1)
    elif i % 2 == 0:
        print(int(pow(2, i)))
