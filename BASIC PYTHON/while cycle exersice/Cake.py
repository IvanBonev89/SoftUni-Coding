shirochina = int(input())
daljina = int(input())
s = shirochina * daljina
peaces = s / 1
current_peaces_2 = 0
current_peaces = input()
while current_peaces != 'STOP':
    current_peaces_2 += int(current_peaces)
    diff = (peaces - int(current_peaces_2))
    if diff <= 0:
        print(f"No more cake left! You need {abs(int(diff))} pieces more.")
        break
    current_peaces = input()
else:
    diff = (peaces - int(current_peaces_2))
    print(f"{abs(int(diff))} pieces are left.")
