# read user input

projection = input()
r = int(input())
c = int(input())
total_money = 0
price = 0

# logic

places = r * c

if projection == 'Premiere':
    price += 12.00
elif projection == 'Normal':
    price += 7.50
elif projection == 'Discount':
    price += 5.00

total_money = price * places
#print
print(f'{total_money:.2f} leva')
