# read user input

n = int(input())
#logic
user_input = int(input())
max = user_input
mini = user_input

for i in range(0, n-1):
    num = int(input())
    if num < mini:
        mini = num
    elif num > max:
        max = num

#output
print(f"Max number: {max}")
print(f"Min number: {mini}")
