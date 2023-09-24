from math import floor
peoples_of_group = int(input())
days = int(input())

money = 0

for i in range(1,days+1):

    if i % 10 == 0:
        peoples_of_group -= 2
    if i % 15 == 0:
        peoples_of_group += 5
    money += 50
    money -= 2 * peoples_of_group
    if i % 3 == 0:
        money -= 3*peoples_of_group
    if i % 5 == 0:
        money += 20 * peoples_of_group
        if i % 3 == 0:
            money -= 2*peoples_of_group

money_person = money / peoples_of_group
print(f"{peoples_of_group} companions received {floor(int(money_person))} coins each.")
