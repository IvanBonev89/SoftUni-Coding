# read user input
import math
x = int(input())
y = float(input())
z = int(input())
worker = int(input())

#logic

vine_area = x * 0.4
kg_fruit = vine_area * y
liter_vine = kg_fruit/2.5
liter_vine_format = math.floor(liter_vine)
left_vine = (abs(liter_vine - z))
left_vine_format = math.floor(left_vine)
left_vine_format2 = math.ceil(left_vine)
vine_worker = math.ceil(left_vine_format2/worker)

#output print
if liter_vine < z:
    print(f"It will be a tough winter! More {left_vine_format} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {liter_vine_format} liters.")
    print(f"{left_vine_format2} liters left -> {vine_worker} liters per person.")
