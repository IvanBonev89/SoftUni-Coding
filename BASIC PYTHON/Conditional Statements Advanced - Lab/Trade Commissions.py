# read user input

city = input()
sales = float(input())
commissions = 0
is_input_correct = True
output = "error"
#logic

if city == 'Sofia':
    if 0<= sales <=500:
     commissions = sales * 0.05
    elif  500<sales<=1000:
     commissions = sales * 0.07
    elif  1000 < sales <= 10000:
     commissions =  sales * 0.08
    elif sales > 10000:
     commissions = sales * 0.12
    else:
        is_input_correct = False
elif city == 'Varna':
    if 0<= sales <=500:
     commissions = sales * 0.045
    elif  500<sales<=1000:
     commissions = sales * 0.075
    elif  1000 < sales <= 10000:
     commissions =  sales * 0.10
    elif sales > 10000:
     commissions = sales * 0.13
    else:
        is_input_correct = False
elif city == 'Plovdiv':
    if 0<= sales <=500:
     commissions = sales * 0.055
    elif  500<sales<=1000:
     commissions = sales * 0.08
    elif  1000 < sales <= 10000:
     commissions =  sales * 0.12
    elif sales > 10000:
     commissions = sales * 0.145
    else:
        is_input_correct = False
else:
    is_input_correct = False

# print user output

if is_input_correct:
    print(f'{commissions:.2f}')
else:
    print(output)

