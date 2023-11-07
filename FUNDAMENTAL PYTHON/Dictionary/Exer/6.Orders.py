dictionary = {}
while True:

    orders = input().split()
    if orders[0] == "buy":
        break
    else:
        name = orders[0]
        price = float(orders[1])
        quantity = int(orders[2])

        if name in dictionary:
            if dictionary[name][1] != price:
                dictionary[name] = (quantity + dictionary[name][0], price)
            else:
                dictionary[name] = (quantity + dictionary[name][0], dictionary[name][1])
        else:
            dictionary[name] = (quantity, price)

for name, (quantity, price) in dictionary.items():
    total_price = quantity * price
    print(f"{name} -> {total_price:.2f}")
