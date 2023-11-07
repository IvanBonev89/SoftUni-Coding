command = input().split(": ")
total_products = 0
total_quantity = 0
new_products = {}
while command[0] != "statistics":
    name = command[0]
    quantity = command[1]
    total_quantity += int(quantity)
    if name not in new_products:
        new_products[name] = 0
        new_products[name] += int(quantity)
        total_products += 1
    else:
        for i in new_products:
            if name == i:
                new_products[name] += int(quantity)
    command = input().split(": ")

print("Products in stock:")
for (product,quantity) in new_products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")