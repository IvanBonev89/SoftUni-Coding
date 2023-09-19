money_need = float(input())
money = float(input())
days = 0
days_count = 0
while True:
    if money < money_need:
        days += 1
        action = input()
        current_money = float(input())
        if action == "spend":
            money -= current_money
            days_count += 1
        if action == 'save':
            money += current_money
            days_count = 0
        if money <= 0:
            money = 0
        if days_count >= 5:
            print("You can't save the money.")
            print(f"{days}")
            break
        if money >= money_need:
            print(f"You saved the money for {days} days.")
            break
