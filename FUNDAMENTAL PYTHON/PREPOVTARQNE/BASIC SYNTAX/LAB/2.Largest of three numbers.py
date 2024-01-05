num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

max = 0

if num_1 >= num_2 and num_1 >= num_3:
    max = num_1
elif num_2 >= num_1 and num_2 >= num_3:
    max = num_2
else:
    max = num_3
print(max)