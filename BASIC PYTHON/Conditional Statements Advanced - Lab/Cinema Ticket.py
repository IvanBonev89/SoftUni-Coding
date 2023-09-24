# read user input
day = input()
price = 0
# logic
if day in ('Monday Tuesday Friday'):
    price = 12
elif day in ('Wednesday Thursday'):
    price = 14
elif day in ('Sunday Saturday'):
    price = 16

# read user output
print(price)
