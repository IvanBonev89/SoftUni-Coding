tax = int(input())
basket_foot = tax - (tax*0.4)
basket_suit = basket_foot - (basket_foot * 0.2)
basket_ball = basket_suit * 0.25
basket_accesoares = basket_ball * 0.2
total_cost = tax + basket_foot + basket_suit + basket_ball + basket_accesoares
print(total_cost)
