country = input().split(", ")
capitals = input().split(", ")
total = zip(country, capitals)
dictionary = {}

for i in total:
    dictionary[i[0]] = i[1]

for key, value in dictionary.items():
    print(f"{key} -> {value}")
