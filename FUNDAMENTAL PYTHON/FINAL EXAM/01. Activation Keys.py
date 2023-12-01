
act_key = input()
command = input()
while command != "Generate":
    if "Slice" in command:
        cmd, index, index_end = command.split(">>>")
        index = int(index)
        index_end = int(index_end)
        if index in range(len(act_key)) and index_end in range(len(act_key)):
            first_part = act_key[:index]
            second_part = act_key[index_end:]
            act_key = first_part + second_part
        print(act_key)

    elif "Flip" in command:
        cmd, up, index, index_end = command.split(">>>")
        index = int(index)
        index_end = int(index_end)
        if index in range(len(act_key)) and index_end in range(len(act_key)):
            if up == "Upper":
                upper_part = act_key[index:index_end].upper()
                first_part = act_key[:index]
                second_part= act_key[index_end:]
                act_key = first_part+upper_part+second_part
            else:
                upper_part = act_key[index:index_end].lower()
                first_part = act_key[:index]
                second_part = act_key[index_end:]
                act_key = first_part + upper_part + second_part
        print(act_key)

    elif "Contains" in command:
        cmd, sub_key = command.split(">>>")
        if sub_key in act_key:
            print(f"{act_key} contains {sub_key}")
        else:
            print("Substring not found!")


    command = input()

print(f"Your activation key is: {act_key}")


#PRINTTTTTTTTTTTTTTTTTTTT DA E NA NIVOTO NA IF