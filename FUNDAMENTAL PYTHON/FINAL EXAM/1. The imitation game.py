encrypted_message = input()
command_full = input()

while command_full != "Decode":
    command_list = command_full.split("|")
    command = command_list[0]
    if command == "ChangeAll":
        change_alpha = command_list[1]
        new_alpha = command_list[2]
        if change_alpha in encrypted_message:
            encrypted_message = encrypted_message.replace(change_alpha,new_alpha)
        else:
            pass
    elif command == "Insert":
        index = int(command_list[1])
        new_al = command_list[2]
        modified_string = encrypted_message[:index] + new_al + encrypted_message[index:]
        encrypted_message = modified_string
    elif command == "Move":
        number = int(command_list[1])
        first_string = encrypted_message[:number]
        last_string = encrypted_message[number:]
        encrypted_message = last_string + first_string
    else:
        command_full = input()
    command_full=input()

print(f"The decrypted message is: {encrypted_message}")