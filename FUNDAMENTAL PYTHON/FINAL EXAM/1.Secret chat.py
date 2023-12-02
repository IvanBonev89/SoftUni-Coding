message = input()
command = input()

while command != "Reveal":

    if "InsertSpace" in command:
        cmd, index = command.split(":|:")
        index = int(index)
        if index in range(len(message)):
            first_part = message[:index]
            second_part = message[index:]
            new_string = " "
            message = first_part + new_string + second_part
        print(message)

    elif "Reverse" in command:
        cmd, substring = command.split(":|:")
        if substring in message:
            new_string = ""
            reverse_string = ''
            for i in range(len(substring) - 1, -1, -1):
                reverse_string += substring[i]
            message = message.replace(substring,new_string)
            message = message + reverse_string
            print(message)
        else:
            print("error")


    elif "ChangeAll" in command:
        cmd, old_string, new_string = command.split(":|:")
        if old_string in message:
            message = message.replace(old_string, new_string)
        print(message)

    command = input()

print(f"You have a new text message: {message}")