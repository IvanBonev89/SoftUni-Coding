phonebook = {}
while True:
    info = input()
    if len(info) < 4:
        number_names = int(info)
        break
    else:
        info_list = info.split("-")
        phonebook[info_list[0]] = info_list[1]


if number_names > 0:
    for num_name in range(1,number_names+1):
        name = input()
        if name not in phonebook.keys():
            print(f"Contact {name} does not exist.")
        else:
            print(f"{name} -> {phonebook[name]}")
