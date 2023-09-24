#read user input

n = int(input())
period = str(input())

#logic

if period == "day":
    taxi_price = 0.70 + 0.79*n
else:
    taxi_price = 0.70 + 0.90*n


bus_price = 0.09 * n

train_price = 0.06 * n

#output print

if n<20:
    print(f"{taxi_price:.2f}")
elif 100> n >= 20:
    print(f"{bus_price:.2f}")
else:
    print(f"{train_price:.2f}")
