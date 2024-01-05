budget = int(input())
command = input()
status = ''
while command != 'End':
    budget -= int(command)
    if budget < 0:
        print("You went in overdraft!")
        status = "bankrupt"
        break
    else:
        command = input()

if status != "bankrupt":
    print("You bought everything needed.")