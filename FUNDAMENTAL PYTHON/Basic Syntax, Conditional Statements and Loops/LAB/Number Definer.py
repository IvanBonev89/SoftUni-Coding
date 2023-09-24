n = float(input())

if 0 < n < 1:
    print("small positive")
elif 1 <= n <= 1000000:
    print("positive")
elif n > 1000000:
    print("large positive")
elif 0 > n > -1:
    print("small negative")
elif n < -1000000:
    print("large negative")
elif -1 >= n >= - 1000000:
    print("negative")
elif n == 0:
    print("zero")
    
