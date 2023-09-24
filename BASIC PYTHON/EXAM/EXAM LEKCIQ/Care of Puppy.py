#input

food_kg = int(input())
fodd_gr = food_kg * 1000
#logic
total_eat_gr = 0
eat_gr = input()

while eat_gr != 'Adopted':
    eat_gr_int = int(eat_gr)
    total_eat_gr += eat_gr_int
    eat_gr = input()

diff = abs(fodd_gr - total_eat_gr)
if total_eat_gr <= fodd_gr:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")