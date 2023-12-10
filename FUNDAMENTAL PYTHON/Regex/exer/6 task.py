import re
text = input()

while text:

    regex = r"www\.[A-Za-z0-9\-\.]+\.[a-z]+\b"
    matches = re.findall(regex, text)
    if matches:
        print(''.join(matches))
    text = input()
