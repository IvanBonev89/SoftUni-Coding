
# input
import math

days = int(input())
food_kg = int(input())
food_1 = float(input())
food_2 = float(input())
food_3 = float(input())
#logic
total_food_1 = days * food_1
total_food_2 = days * food_2
total_food_3 = days * food_3

total_food = total_food_1 + total_food_2 + total_food_3
diff = abs(food_kg - total_food)
#output
if food_kg >= total_food:
    diff_1 = math.floor(diff)
    print(f'{diff_1} kilos of food left.')
else:
    diff_2 = math.ceil(diff)
    print(f'{diff_2} more kilos of food are needed.')

