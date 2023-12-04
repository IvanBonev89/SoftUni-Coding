import re
text = input()
word = input()

pattern = fr"(?i)\b{word}\b"
matches = re.findall(pattern,text)
counter = len(matches)
print(counter)