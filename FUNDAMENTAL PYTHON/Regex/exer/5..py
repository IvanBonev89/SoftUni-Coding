import re

command = input()
matches = []
items = []
money = []
total_money = 0

while command != "Purchase":
    regex = r">>([^<>]+)<<(\d+\.?\d*)!(\d+)"
    new_matches = re.findall(regex, command)
    matches.extend(new_matches)  # Append new matches to the existing list

    for match in matches:
        furniture_name, price, quantity = match  # Extract information from each match
        items.append(furniture_name)
        money.append(float(price) * float(quantity))
        matches = []

    command = input()
print("Bought furniture:")
for j in items:

    print("".join(j),end= "\n")
for i in money:
    total_money += float(i)
print(f"Total money spend: {total_money:.2f}")
