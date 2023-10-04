string = input()
new_string = []
string_list = list(string.split())
for i in string_list:
    int_num = int(i)
    opposite_num = int_num * (-1)
    new_string.append(opposite_num)

print(new_string)


#
