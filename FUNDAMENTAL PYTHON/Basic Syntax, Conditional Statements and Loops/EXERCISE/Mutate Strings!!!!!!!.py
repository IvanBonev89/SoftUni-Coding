string1 = input()
string2 = input()
last_string = string1

for i in range(0,len(string1)):
    #print(f"index = {i} letter = {string1[i]}")
    left_part = string2[0:i+1]
    right_part = string1[i+1:]
    new_string = left_part + right_part
    if new_string == last_string:
        continue
    print(new_string)
    last_string = new_string
