# read user input
day = input()
is_valid_input = True
#logic
if day in ("Monday Tuesday Wednesday Thursday Friday"):
  print("Working day")
elif day in ("Sunday Saturday"):
    print("Weekend")
else:
    print("Error")
#print user output
if is_valid_input == False:
    print("Error")
