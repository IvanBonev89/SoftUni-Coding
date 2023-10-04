string = input().split()
n = int(input())
string_int = []
for i in string:
    string_int.append(int(i))

for index in range(n):
    string_int.remove(min(string_int))

final_numbers = ''

for i in range(len(string_int)):
    if i == len(string_int) - 1:
        final_numbers += str(string_int[i])
    else:
        final_numbers += str(string_int[i]) +', '


print(final_numbers)
