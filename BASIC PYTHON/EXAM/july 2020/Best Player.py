# input
name = input()
is_valid = False
max_goals = 0
max_goal_name = ''
hatrick = ''
while name != 'END':
    goals = int(input())
    if goals > max_goals:
        max_goals = goals
        max_goal_name = name
        is_valid = True
        if goals >= 3:
            hatrick = 'YES'
    if max_goals >= 10:
        break
    name = input()
    if name == "END":
       is_valid = True
       break

print(f"{max_goal_name} is the best player!")
if hatrick == "YES":
 print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
 print(f"He has scored {max_goals} goals.")

