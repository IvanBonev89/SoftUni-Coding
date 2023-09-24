# read user input
import math
n = int(input())
food = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input())

#logic
turtle_food_kg = turtle_food/1000
total_food = (dog_food + cat_food + turtle_food_kg)*n
left_food = math.floor(abs(total_food - food))
left_food2 = math.ceil(abs(total_food - food))

#output print
if total_food<= food:
    print(f"{left_food} kilos of food left.")
else:
    print(f"{left_food2} more kilos of food are needed.")


