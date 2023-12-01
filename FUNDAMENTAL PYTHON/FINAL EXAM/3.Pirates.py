collection = {}
info = input()
cmd = ''

while info != "Sail":
    city, population, gold = info.split("||")
    if city in collection:
        collection[city][0] += int(population)
        collection[city][1] += int(gold)
    else:
        collection[city] = [int(population), int(gold)]
    info = input()

events = input()

while events != "End":
    if "Plunder" in events:
        cmd, city, population, gold = events.split("=>")
        if city in collection:

            collection[city][0] -= int(population)
            collection[city][1] -= int(gold)
            print(f"{city} plundered! {gold} gold stolen, {population} citizens killed.")
            if collection[city][0] <= 0 or collection[city][1] <= 0:
                collection.pop(city)
                print(f"{city} has been wiped off the map!")
    elif "Prosper" in events:
        cmd, city, gold = events.split("=>")
        if city in collection:
            if int(gold) >= 0:
                collection[city][1] += int(gold)
                print(f"{gold} gold added to the city treasury. {city} now has {collection[city][1]} gold.")
            else:
                print("Gold added cannot be a negative number!")
    events = input()
if len(collection) > 0:
    print(f"Ahoy, Captain! There are {len(collection)} wealthy settlements to go to:")
    for city, population in collection.items():
        print(f"{city} -> Population: {collection[city][0]} citizens, Gold: {collection[city][1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

# bqh napisal if len(collection) > 0 pod print-a i davashe 92
