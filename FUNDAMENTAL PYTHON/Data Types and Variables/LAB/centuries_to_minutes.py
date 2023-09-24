centuries = int(input())
years = centuries * 100
days = 365.2422 * years
hours = int(days) * 24
minutes = hours * 60

print(f"{int(centuries)} centuries = {int(years)} years = {int(days)} days = {int(hours)} hours = {int(minutes)} minutes")

