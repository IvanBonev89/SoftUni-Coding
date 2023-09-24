deposit_sum = float(input())
deposit_month = int(input())
percent_rate = float(input())
rate = percent_rate/100
total_sum = deposit_sum + deposit_month*(deposit_sum*rate/12)
print(total_sum)



