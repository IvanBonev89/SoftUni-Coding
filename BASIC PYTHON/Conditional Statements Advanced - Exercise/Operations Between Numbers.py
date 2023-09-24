# read user input

n1 = int(input())
n2 = int(input())
operator = input()
result = 0
result_2 = ''
#logic

if operator == '+':
    result = n1 + n2
elif operator == '-':
    result = n1 - n2
elif operator == '*':
    result = n1 * n2

if result % 2 == 0:
    result_2 = 'even'
else:
    result_2 = 'odd'

if operator in('+ - *'):
    print(f"{n1} {operator} {n2} = {result} - {result_2}")
elif operator == '/':
    if n2 == 0:
       print(f'Cannot divide {n1} by zero')
    else:
     result = n1 / n2
     print(f"{n1} / {n2} = {result:.2f}")

elif operator == '%':
    if n2 == 0:
       print(f'Cannot divide {n1} by zero')
    else:
     result = n1 % n2
     print(f"{n1} % {n2} = {result}")
