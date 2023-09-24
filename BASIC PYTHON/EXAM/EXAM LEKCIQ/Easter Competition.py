# input

number_breads = int(input())
total_points = 0
max_points = 0
name_1 = ''

for peoples in range(1, number_breads + 1):
    name = input()
    ocenka = input()
    total_points = 0
    while ocenka != 'Stop':
        ocenka_int = int(ocenka)
        total_points += ocenka_int
        ocenka = input()
    print(f"{name} has {total_points} points.")
    if total_points > max_points:
        max_points = total_points
        print(f"{name} is the new number 1!")
        name_1 = name
print(f"{name_1} won competition with {max_points} points!")