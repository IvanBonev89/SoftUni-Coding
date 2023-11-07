dictionary = {}
while True:
    word = input()
    if word == "stop":
        break
    value = int(input())
    if word not in dictionary:
        dictionary[word] = value
    else:
        dictionary[word] += int(value)

for key, value in dictionary.items():
    print(f"{key} -> {value}")
