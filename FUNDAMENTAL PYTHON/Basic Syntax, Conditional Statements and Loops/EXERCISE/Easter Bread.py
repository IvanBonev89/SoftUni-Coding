budget = float(input())
price_flour = float(input())
price_eggs = price_flour * 0.75
price_milk = price_flour * 1.25
cost_bread = price_eggs + price_flour + (price_milk/4)
eggs = 0
money = budget
breads = 0

while budget >= cost_bread:
    breads += 1
    budget -= cost_bread
    eggs += 3
    if breads % 3 == 0:
        eggs -= breads - 2

print(f"You made {breads} loaves of Easter bread! Now you have {eggs} eggs and {budget:.2f}BGN left.")

