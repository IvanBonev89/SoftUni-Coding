tabs = int(input())
salary = float(input())
penalty = 0
for current_tab in range(tabs):
    website = input()
    if website == 'Facebook':
        penalty += 150
    elif website == 'Instagram':
        penalty += 100
    elif website == 'Reddit':
        penalty += 50
    if (salary - penalty) <= 0:
        break


diff = salary - penalty
if salary - penalty > 0:
    print(int(diff))
else:
    print("You have lost your salary.")
