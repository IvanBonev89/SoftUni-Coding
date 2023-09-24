name_actor = input()
points = float(input())
members = int(input())


for competition in range(members):
    name_member = input()
    point_member = float(input())
    total_point_member = (len(name_member) * point_member) /2
    points += total_point_member
    if points > 1250.5:
        break

diff = 1250.5 - points
if points > 1250.5:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {points:.1f}!")
else:
    print(f"Sorry, {name_actor} you need {diff:.1f} more!")
