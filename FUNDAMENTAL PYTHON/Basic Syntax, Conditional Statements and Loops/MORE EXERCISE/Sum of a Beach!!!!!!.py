word = input()
count = 0
list = ["Sand", "Water", "Fish", "Sun"]

word_1 = word.lower()
if list[0].lower() in word_1:
    count += 1
if list[1].lower() in word_1:
    count += 1
if list[2].lower() in word_1:
    count += 1
if list[3].lower() in word_1:
    count += 1

print(count)
