import re
valid_date = []
date = input()
valid = "(\\d{2})([/.-])([A-Z][a-z]{2})\\2(\\d{4}\\b)"
matches = re.findall(valid, date)

for i in matches:
    separate = i[1]
    day = i[0]
    month = i[2]
    year = i[3]
    print(f"Day: {day}, Month: {month}, Year: {year}")

