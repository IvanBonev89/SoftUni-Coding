n = int(input())
total_price = 0
for deals in range(n):
    price_caps = float(input())
    days = int(input())
    caps = int(input())
    if 0.01 <= price_caps <= 100.00 and 1<= days <= 31 and 1<= caps <= 2000:
        price = price_caps * days * caps
        total_price += price
        print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total_price:.2f}")
