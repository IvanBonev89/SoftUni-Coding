#input

month = int(input())
total_cost = 0
# logic
electricity_total = 0
water = 0
internet = 0
other = 0
for balance in range(1, month + 1):
    electricity = float(input())
    electricity_total += electricity
    water_month = 20
    water += water_month
    internet_month = 15
    internet += internet_month
    total_month = (electricity + water_month + internet_month)
    p_total_month = total_month * 0.2
    other_month = total_month + p_total_month
    other += other_month
    total_cost += (electricity + water_month + internet_month + other_month)

avg = total_cost / month

print(f"Electricity: {electricity_total:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {avg:.2f} lv")

