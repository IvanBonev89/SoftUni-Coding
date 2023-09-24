number = int(input())
digits = sorted(str(number), reverse=True)
largest_number = ""
for digit in digits:
  largest_number += digit
print(largest_number)
