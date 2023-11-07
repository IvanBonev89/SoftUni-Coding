items = input().split()
materials = {}
status = ''
junks = {}

def legendary_status(material):
    global status
    if material.lower() == "shards":
        status = "Shadowmourne"
    if material.lower() == "fragments":
        status = "Valanyr"
    if material.lower() == "motes":
        status = "Dragonwrath"


for i in range(0, len(items), 2):
    quantity = int(items[i])
    material = items[i + 1].lower()
    if material in materials and material in["shards","fragments","motes"]:
        materials[material] += quantity
        if materials[material] >= 250:
            legendary_status(material)
            break
    if material not in materials and material in ["shards", "fragments", "motes"]:
        materials[material] = quantity
        if materials[material] >= 250:
            legendary_status(material)
            break
    if material in junks and material not in ["shards", "fragments", "motes"]:
        junks[material] += quantity
    if material not in junks and material not in ["shards", "fragments", "motes"]:
        junks[material] = quantity

print(f"{status} obtained!")
for material, quantity in materials.items():
    print(f"{material}: {quantity}")
for material, quantity in junks.items():
    print(f"{material}: {quantity}")