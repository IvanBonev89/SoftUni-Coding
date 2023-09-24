price_vegetables = float(input())
price_fruits = float(input())
kilogram_vegetables = int(input())
kilogram_fruits = int(input())
profit_vegetables = price_vegetables * kilogram_vegetables
profit_fruits = price_fruits*kilogram_fruits
profit_bgn = profit_vegetables + profit_fruits
profit_eur = profit_bgn/1.94
print(f"{profit_eur:.2f}")



