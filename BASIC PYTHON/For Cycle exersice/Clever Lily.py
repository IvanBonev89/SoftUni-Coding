age = int(input())
price_product = float(input())
price_toy = int(input())
toys = 0
money = 0
current_money = 0
for birthday in range(1,age+1):
    if birthday % 2 != 0:
        toys += 1
    else:
        current_money += 10
        money += current_money - 1


money_from_gift = toys * price_toy
total_money = money_from_gift + money
diff = abs(total_money - price_product)
if total_money>= price_product:
   print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")

