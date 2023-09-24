# read user input

fruit = input()
day = input()
quantity = float(input())
price = 0
#logic



if fruit == 'banana' and day in ("Monday Tuesday Wednesday Thursday Friday"):
    price = quantity * 2.50
    print(f"{price:.2f}")
elif fruit == 'apple' and day in ("Monday Tuesday Wednesday Thursday Friday"):
    price = quantity * 1.20
    print(f"{price:.2f}")
elif fruit == 'orange' and day in ("Monday Tuesday Wednesday Thursday Friday"):
    price = quantity * 0.85
    print(f"{price:.2f}")
elif fruit == 'grapefruit' and day in ("Monday Tuesday Wednesday Thursday Friday"):
    price = quantity * 1.45
    print(f"{price:.2f}")
elif fruit == 'kiwi' and day in ("Monday Tuesday Wednesday Thursday Friday"):
    price = quantity * 2.70
    print(f"{price:.2f}")
elif fruit == 'pineapple' and day in ("Monday Tuesday Wednesday Thursday Friday"):
    price = quantity * 5.50
    print(f"{price:.2f}")
elif fruit == 'grapes' and day in ("Monday Tuesday Wednesday Thursday Friday"):
    price = quantity * 3.85
    print(f"{price:.2f}")
elif fruit == 'banana' and day in ("Saturday Sunday"):
    price = quantity * 2.70
    print(f"{price:.2f}")
elif fruit == 'apple' and day in ("Saturday Sunday"):
    price = quantity * 1.25
    print(f"{price:.2f}")
elif fruit == 'orange' and day in ("Saturday Sunday"):
    price = quantity * 0.90
    print(f"{price:.2f}")
elif fruit == 'grapefruit' and day in ("Saturday Sunday"):
    price = quantity * 1.60
    print(f"{price:.2f}")
elif fruit == 'kiwi' and day in ("Saturday Sunday"):
    price = quantity * 3.00
    print(f"{price:.2f}")
elif fruit == 'pineapple' and day in ("Saturday Sunday"):
    price = quantity * 5.60
    print(f"{price:.2f}")
elif fruit == 'grapes' and day in ("Saturday Sunday"):
    price = quantity * 4.20
    print(f"{price:.2f}")
else:
    print("error")
