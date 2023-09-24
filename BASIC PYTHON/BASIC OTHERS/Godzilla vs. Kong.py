# read user input
budget = float(input())
persons = int(input())
price_clothes = float(input())

#logical

decor = budget * 0.10
if persons >= 150:
    discount_clothes = price_clothes * 0.1
    price_clothes -= discount_clothes

total_cost = decor + price_clothes * persons
money = abs(budget - total_cost)

#output print
if total_cost > budget:
    print("Not enough money!")
    print(f"Wingard needs {money:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {money:.2f} leva left.")
