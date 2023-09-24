word = input()
count = 0
list = ["Sand", "Water", "Fish", "Sun"]

word_1 = word.lower()
list0 = list[0].lower()
list1 = list[1].lower()
list2 = list[2].lower()
list3 = list[3].lower()
if list0  in word_1:
    count += word_1.count(list0)
if list[1].lower() in word_1:
    count += word_1.count(list1)
if list[2].lower() in word_1:
    count += word_1.count(list2)
if list[3].lower() in word_1:
    count += word_1.count(list3)

print(count)
