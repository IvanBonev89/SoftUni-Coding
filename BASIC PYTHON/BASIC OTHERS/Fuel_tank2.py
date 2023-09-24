fuel = str(input())
liters = float(input())
card = str(input())

price = 0
discount = 0
total_price = 0

if fuel == "Gas":
 price = 0.93 * liters

if fuel == "Gasoline":
 price = 2.22 * liters

if fuel == "Diesel":
 price = 2.33 * liters


if fuel == "Gas" and card == "Yes":
    price -= (0.08 * liters)
if fuel == "Gasoline" and card == "Yes":
    price -= (0.18 * liters)
if fuel == "Diesel" and card == "Yes":
    price -= (0.12 * liters)

if 20<= liters <= 25:
    discount = price * 0.08
    total_price = price - discount
elif 25 < liters:
    discount = price * 0.10
total_price = price - discount

print(f"{total_price:.2f} lv.")
