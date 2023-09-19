money = int(input())
price = input()
count = 0
price_cash = 0
price_cash_counter = 0
price_card = 0
price_card_counter = 0
while price != 'End':
    price_int = int(price)
    count += 1
    if count % 2 != 0:
        if price_int <= 100:
            price_cash += price_int
            price_cash_counter += 1
            print("Product sold!")
        else:
            print("Error in transaction!")
    else:
        if price_int >= 10:
            price_card += price_int
            price_card_counter += 1
            print("Product sold!")
        else:
            print("Error in transaction!")
    if money <= price_cash + price_card:
        total_counter = price_card_counter + price_cash_counter
        avg_cash = price_cash  / price_cash_counter
        avg_card = price_card / price_card_counter
        print(f"Average CS: {avg_cash:.2f}")
        print(f"Average CC: {avg_card:.2f}")
        break
    else:
        price = input()
else:
    print("Failed to collect required money for charity.")
