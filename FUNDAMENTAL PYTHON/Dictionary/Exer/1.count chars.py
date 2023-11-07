word = input()
dictionary = {}
for i in word:
    counter = word.count(i)
    if i not in dictionary and i != " ":
        dictionary[i] = counter

for key, value in dictionary.items():
    print(f"{key} -> {value}")
