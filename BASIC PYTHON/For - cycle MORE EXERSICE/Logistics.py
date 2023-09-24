freight = int(input())
vehicle = ''
price = 0
total_price = 0
total_tons = 0
bus_tons = 0
truck_tons = 0
train_tons = 0
for logistic in range(freight):
    tons = int(input())
    if tons <= 3:
        vehicle = 'bus'
        price = 200
        bus_tons += tons
        total_price += price * tons
        total_tons += tons
    if 4 <= tons <= 11:
        vehicle = 'truck'
        price = 175
        truck_tons += tons
        total_price += price * tons
        total_tons += tons
    if 12 <= tons:
        vehicle = 'train'
        price = 120
        train_tons += tons
        total_price += price * tons
        total_tons += tons

avg_price = total_price / total_tons

p_bus = bus_tons / total_tons * 100
p_truck = truck_tons / total_tons * 100
p_train = train_tons / total_tons * 100

print(f'{avg_price:.2f}')
print(f'{p_bus:.2f}%')
print(f'{p_truck:.2f}%')
print(f'{p_train:.2f}%')
