import re
text = input()

while text:

    regex = r"www\.[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,6}\.[a-zA-Z]{2,6}?\/.*?"
    matches = re.findall(regex, text)
    if matches:
        print(''.join(matches))
    text = input()
