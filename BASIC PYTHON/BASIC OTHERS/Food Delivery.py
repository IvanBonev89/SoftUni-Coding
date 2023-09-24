number_chicken = int(input())
number_fish = int(input())
number_vegan = int(input())

price_chicken = number_chicken * 10.35
price_fish = number_fish * 12.40
price_vegan = number_vegan * 8.15

sum_price = price_vegan + price_fish + price_chicken

desert = sum_price * 0.2
total_price = sum_price + desert + 2.50
print("цена на поръчката")
print(round(total_price,2))






