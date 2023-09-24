# read user input
import math
magnol = int(input())
zumbul = int(input())
rose = int(input())
cactus = int(input())
price = float(input())

#logic

total_price = magnol * 3.25 + zumbul * 4 + rose * 3.50 + cactus *8
tax = total_price * 0.05
budget = total_price - tax
left_price = math.floor(abs(budget - price))
left_price2 = math.ceil(abs(budget - price))
if budget >= price:
    print(f"She is left with {left_price} leva.")
else:
    print(f"She will have to borrow {left_price2} leva.")

