text = input()

command = input()

while command != "End":
    if "Translate" in command:
        cmd, char, replacement = command.split(" ")
        if char in text:
            text = text.replace(char, replacement)
            print(text)
    elif "Includes" in command:
        cmd, substring = command.split(" ")
        if substring in text:
            print("True")
        else:
            print("False")
    elif "Start" in command:
        cmd, substring = command.split(" ")
        if text.startswith(substring):
            print("True")
        else:
            print("False")
    elif "Lowercase" in command:
        text = text.lower()
        print(text)
    elif "FindIndex" in command:
        cmd, char = command.split(" ")
        last_occurrence_index = text.rfind(char)
        print(last_occurrence_index)
    elif "Remove" in command:
        cmd, index, count = command.split(" ")
        index = int(index)
        count = int(count)
        if 0 <= index < len(text):
            modified_string = text[:index] + text[index + count:]
            text = modified_string
            print(text)
    command = input()
