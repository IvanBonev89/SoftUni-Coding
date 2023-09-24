# read user input

num = int(input())
is_input_valid = True
#logic
if 7 >= num >= 1:
    if num == 1:
     print("Monday")
    elif num == 2:
      print("Tuesday")
    elif num == 3:
      print("Wednesday")
    elif num == 4:
       print("Thursday")
    elif num == 6:
        print("Saturday")
    elif num == 5:
        print("Friday")
    elif num == 7:
        print ("Sunday")
else:
    is_input_valid = False
# print output user
    print("Error")
