capacity_tank_water = 255
number_cycle = int(input())
sum_water = 0
sum_water_in_tank = 0
for i in range(number_cycle):
    water = int(input())
    sum_water += water
    if (water+sum_water_in_tank) > capacity_tank_water:
        print("Insufficient capacity!")
    else:
        sum_water_in_tank += water

print(sum_water_in_tank)

