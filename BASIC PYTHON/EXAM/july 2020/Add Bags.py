# input

price_over_20kg = float(input())
bags_kg = float(input())
days = int(input())
bags_number = int(input())
price = 0

if bags_kg < 10:
    price = price_over_20kg * 0.2
elif 20 >= bags_kg >= 10:
    price = price_over_20kg * 0.5
elif bags_kg > 20:
    price = price_over_20kg

if days > 30:
    price = price * 1.10
elif 7 <= days <= 30:
    price = price * 1.15
elif days < 7:
    price = price * 1.40

total_price = price * bags_number

# output

print(f"The total price of bags is: {total_price:.2f} lv.")
