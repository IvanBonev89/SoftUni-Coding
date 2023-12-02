password = input()
command = input()
new_pass = ""
while command != "Done":
    if "TakeOdd" in command:
        for i in range(0, len(password)):
            if i % 2 != 0:
                new_pass += password[i]
        password = new_pass
        print(password)

    elif "Cut" in command:
        cmd, index, length = command.split(" ")
        index = int(index)
        length = int(length)
        substring_1 = password[:index]
        substring_2 = password[index+length:]
        password = substring_1 + substring_2
        print(password)
    elif "Substitute" in command:
        cmd, substring, substitute = command.split(" ")
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {password}")
