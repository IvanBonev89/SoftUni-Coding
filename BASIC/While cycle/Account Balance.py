sum = 0

while True:
    money = input()
    if money == 'NoMoreMoney':
        print(f"Total: {sum:.2f}")
        break
    money_real = float(money)
    if money_real > 0:
        sum += money_real
        print(f"Increase: {money_real:.2f}")
    else:
        print("Invalid operation!")
        print(f"Total: {sum:.2f}")
        break

