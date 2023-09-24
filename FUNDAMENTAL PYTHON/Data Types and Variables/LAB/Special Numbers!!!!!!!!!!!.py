n = int(input())
result = ""
number = 0

for i in range(1 ,n+1):
    sum = 0
    digits = i
    while digits > 0:
        sum += digits % 10
        digits = int(digits//10)
        if sum == 5 or sum == 7 or sum == 11:

            result = True
        else:
            result = False
    print(f"{i} -> {result}")

"""
 variant da e string

for i in range(1, n+1):
  strin_n = str(n)
   digit_sum = 0
    for digit in strin_n:
        digit_sum += (int(digit))
        if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
          result = True
       else:
            result = False
   print(f"{i} -> {result}")


"""