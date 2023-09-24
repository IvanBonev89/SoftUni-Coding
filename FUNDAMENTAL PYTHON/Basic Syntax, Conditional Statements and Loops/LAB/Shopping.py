budget = int(input())
command = input()
while command != "End":
    cost = int(command)
    budget -= cost
    if budget < 0:
        print("You went in overdraft!")
        break
    else:
        command = input()
if budget >= 0:
    print("You bought everything needed.")
