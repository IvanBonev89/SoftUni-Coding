import re

n = int(input())
valid_list = []
string = ''
string1 = ''
for i in range(n):
    info = input()
    regex = r"([$]{1}|[%]{1})([A-Z]{1}[a-z]+\1\: \[\d+\]\|\[\d+\]\|\[\d+\]\|){0,3}$"
    match = re.finditer(regex, info)
    valid_message_found = False

    for j in match:
        new_emoji = j.group(1) + j.group(2)
        valid_list.append(new_emoji)
        cmd, digits = new_emoji.split(": ")
        digit = digits.split("|")
        for num in digit:
            regex1 = r'\[(\d+)\]'
            match = re.search(regex1, num)
            if match:
                number = int(match.group(1))
                if number >= 1 or number <= 255:
                    ascii = chr(number)
                    string += ascii
        for s in cmd:
            if s.isalpha():
                string1 += s

        if info in valid_list:
            valid_message_found = True
            print(f"{string1}: {string}")
            string = ''
            string1 = ''

    if not valid_message_found:
        print("Valid message not found!")
