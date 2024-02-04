number_coffe = int(input())
total_price = 0
status = ''
for i in range(1,number_coffe+1):
    price = float(input())
    days = int(input())
    capsules = int(input())
    if 0.01 <= price <= 100.00 and 1 <= days <= 31 and 1 <= capsules <= 2000:
        caps_month = days*capsules
        cost = caps_month * price
        total_price += cost
        print(f"The price for the coffee is: ${cost:.2f}")


print(f"Total: ${total_price:.2f}")
