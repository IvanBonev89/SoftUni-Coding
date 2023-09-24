# input

name = input()
tickets_old = int(input())
tickets_kid = int(input())
price_old = float(input())
price_usluga = float(input())
#logic
price_kid = price_old * 0.3
total_old = tickets_old * (price_old + price_usluga)
total_kid = tickets_kid * (price_kid + price_usluga)
total_price = total_kid + total_old
profit = total_price * 0.2

# print

print(f"The profit of your agency from {name} tickets is {profit:.2f} lv.")
