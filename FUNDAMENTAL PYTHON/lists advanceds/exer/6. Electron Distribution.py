electrons = int(input())

# Инициализирай празен списък за обвивките
shells = []

# Процес на разпределение на електроните по обвивките
n = 1
while electrons > 0:
    max_electrons = 2 * n ** 2
    if electrons >= max_electrons:
        shells.append(max_electrons)
        electrons -= max_electrons
    else:
        shells.append(electrons)
        electrons = 0
    n += 1

# Изведи попълнените обвивки
print(shells)