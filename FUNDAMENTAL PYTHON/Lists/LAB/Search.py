number = int(input())
word = input()
list = []
list_sorted = []

for i in range (1, number+1):
    text = input()
    list.append(text)
    if word in text:
        list_sorted.append(text)

print(list)
print(list_sorted)