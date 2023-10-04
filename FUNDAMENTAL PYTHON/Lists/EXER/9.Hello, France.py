ticket = 150
percent = 40
sum = 0
buy = []
sell = []
price = 0
costs = 0
collection = input().split("|")
budget = float(input())
for products in collection:
    type_product = products.split("->")
    type_p = type_product[0]
    price_p = float(type_product[1])
    if type_p == 'Clothes':
        if price_p <= 50.00:
            if budget >= price_p:
                budget -= price_p
                buy.append(price_p)
                costs += price_p
    if type_p == 'Shoes':
        if price_p <= 35.00:
            if budget >= price_p:
                budget -= price_p
                buy.append(price_p)
                costs += price_p
    if type_p == 'Accessories':
        if price_p <= 20.50:
            if budget >= price_p:
                budget -= price_p
                buy.append(price_p)
                costs += price_p

for j in buy:
    new_price = float(j) *1.40
    sum += new_price
    sell.append(new_price)

#print(*sell) # vajnoooooooooooo
print(" ".join([format(number, ".2f") for number in sell])) # vajnoooo


total_budget = budget + sum
result = total_budget - ticket
profit = sum - costs
print(f"Profit: {profit:.2f}")
if result >= 0:
    print("Hello, France!")
else:
    print("Not enough money.")
