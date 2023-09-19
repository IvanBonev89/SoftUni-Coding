money = float(input())
money_monets = int(money * 100)
coin_counter = 0
while True:
    if money_monets >= 200:
        coin_counter += 1
        money_monets -= 200
    elif 199 >= money_monets >= 100:
        coin_counter += 1
        money_monets -= 100
    elif 99 >= money_monets >= 50:
        coin_counter += 1
        money_monets -= 50
    elif 49 >= money_monets >= 20:
        coin_counter += 1
        money_monets -= 20
    elif 19 >= money_monets >= 10:
        coin_counter += 1
        money_monets -= 10
    elif 9>= money_monets >= 5:
        coin_counter +=1
        money_monets -= 5
    elif 4 >= money_monets >= 2:
        coin_counter += 1
        money_monets -= 2
    elif 1 == money_monets:
        coin_counter += 1
        money_monets -= 1
    if money_monets == 0:
        break
print(coin_counter)
