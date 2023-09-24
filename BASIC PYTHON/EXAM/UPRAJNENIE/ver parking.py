# Read the number of days and the number of hours for each day
number_of_days = int(input())
number_of_hours_per_day = int(input())
for i in range(number_of_days):
  number_of_hours_per_day.append(int(input("Enter the number of hours for day {}: ".format(i + 1))))

# Calculate the total cost for each day
total_cost_per_day = []
for i in range(number_of_days):
  day_number = i + 1
  for j in range(number_of_hours_per_day[i]):
    hour_number = j + 1
    if day_number % 2 == 0 and hour_number % 2 == 1:
      total_cost_per_day.append(2.50)
    elif day_number % 2 == 1 and hour_number % 2 == 0:
      total_cost_per_day.append(1.25)
    else:
      total_cost_per_day.append(1.00)

# Calculate the total cost for all days
total_cost = sum(total_cost_per_day)

# Print the results
for i in range(number_of_days):
  print("Day: {} - {} leva".format(i + 1, round(total_cost_per_day[i], 2)))
print("Total: {} leva".format(round(total_cost, 2)))