string = input().split()
shuffles = int(input())
new_list = []
last_list = []
lenght = len(string)
half_lenght = lenght // 2
first_half = string[:half_lenght]
second_half = string[half_lenght:]
for i in range(1, shuffles+1):
    for j in range(0, half_lenght):
        new_list.append(first_half[j])
        new_list.append(second_half[j])
    last_list = new_list.copy()
    new_list = []
    first_half = last_list[:half_lenght]
    second_half = last_list[half_lenght:]

print(last_list)
