def sort_names(names):
    sorted_list = sorted(names, key=lambda x: (-len(x), x))
    return sorted_list

names = input().split(",")
names = [name.strip() for name in names]


print(sort_names(names))
