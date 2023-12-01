import re
need_nutrition = 2000
total_nutrition = 0
info = input()
regex = r"([\|#])([a-zA-Z ]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1"
matches = re.findall(regex,info)
for i in matches:
        total_nutrition += int(i[3])
days = total_nutrition // 2000
print(f"You have food to last you for: {days} days!")

for i in matches:
        items = i[1]
        date = i[2]
        nutrition = i[3]
        print(f"Item: {items}, Best before: {date}, Nutrition: {nutrition}")
