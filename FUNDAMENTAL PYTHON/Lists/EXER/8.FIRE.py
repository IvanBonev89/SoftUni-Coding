fire_info = input().split("#")
water = int(input())
effort = 0
fire = []
total_fire = 0

for info in fire_info:
    type_string, value_str = info.split(" = ")
    value = int(value_str)

    fire_ranges = {"High": (81, 125), "Medium": (51, 80), "Low": (1, 50)}

    if type_string in fire_ranges and fire_ranges[type_string][0] <= value <= fire_ranges[type_string][1]:
        if water >= value:
            water -= value
            effort += value * 0.25
            fire.append(value)
            total_fire += value

print("Cells:")
if fire:
    print("\n".join(f"- {cell}" for cell in fire))
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")