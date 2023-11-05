def which_are_in(input_list, input_list2):
    new_list = []
    for i in input_list:
        for j in input_list2:
            if i in j:
                new_list.append(i)
                break
    return new_list




input_list = input().split(", ")
input_list2 = input().split(", ")
print(which_are_in(input_list, input_list2))
