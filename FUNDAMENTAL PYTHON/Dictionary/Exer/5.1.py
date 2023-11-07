materials = {"shards": 0, "fragments": 0, "motes": 0}
legendary_item = ""


def obtain_legendary_item(material):
    global legendary_item
    if material == "shards" and materials[material] >= 250:
        legendary_item = "Shadowmourne"
    elif material == "fragments" and materials[material] >= 250:
        legendary_item = "Valanyr"
    elif material == "motes" and materials[material] >= 250:
        legendary_item = "Dragonwrath"


junks = {}

while legendary_item == "":
    line = input().lower()
    tokens = line.split()

    for i in range(0, len(tokens), 2):
        quantity = int(tokens[i])
        material = tokens[i + 1]

        if material in materials:
            materials[material] += quantity
            obtain_legendary_item(material)
            if legendary_item:
                break
        else:
            if material in junks:
                junks[material] += quantity
            else:
                junks[material] = quantity

if legendary_item:
    print(f"{legendary_item.capitalize()} obtained!")

key_materials = ["shards", "fragments", "motes"]
for material in key_materials:
    if materials[material] >= 250:
        print(f"{material}: {materials[material] - 250}")
    else:
        print(f"{material}: {materials[material]}")

junks = {k: v for k, v in junks.items() if k not in key_materials}
for material, quantity in junks.items():
    print(f"{material}: {quantity}")
