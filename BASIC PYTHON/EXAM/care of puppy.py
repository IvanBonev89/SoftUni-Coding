food = int(input())
food_grams = food * 1000
is_valid = False
total_eat = 0
eat_int = 0
while True:
    eat = input()

    if eat == 'Adopted':
        is_valid = True
        break
    else:
        eat_int = int(eat)
        total_eat += eat_int
diff = abs(food_grams - total_eat)
if is_valid:
    if total_eat <= food_grams:
         print(f"Food is enough! Leftovers: {diff} grams.")
    else:
        print(f"Food is not enough. You need {diff} grams more.")

