money = input().split(', ')
beggars = int(input())
money_as_int = []
final_sum = []

for i in money:
    money_as_int.append(int(i))
start_index = 0
while start_index < beggars:
    current_beggar_sum = 0
    for current_index in range(start_index, len(money_as_int),beggars):
        current_beggar_sum += money_as_int[current_index]
    final_sum.append(current_beggar_sum)
    start_index += 1

print(final_sum)

