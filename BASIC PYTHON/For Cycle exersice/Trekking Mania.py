num_groups = int(input())
name = ''
total_num = 0
member_musala = 0
member_monblan = 0
member_kilimanjaro = 0
member_k2 = 0
member_everest = 0
for expedition in range (num_groups):
    num_members = int(input())
    if num_members <= 5:
        name = 'Musala'
        member_musala += num_members
    elif 6 <= num_members <= 12:
        name = 'Monblan'
        member_monblan += num_members
    elif 13 <= num_members <= 25:
        name = 'Kilimanjaro'
        member_kilimanjaro += num_members
    elif 26 <= num_members <= 40:
        name = 'K2'
        member_k2 += num_members
    elif 41 <= num_members:
        name = 'Everest'
        member_everest += num_members

total_num = member_musala + member_monblan + member_kilimanjaro + member_k2 + member_everest
p_musala = member_musala / total_num * 100
p_monblan = member_monblan / total_num * 100
p_kilimanjaro = member_kilimanjaro / total_num * 100
p_k2 = member_k2 / total_num * 100
p_everest = member_everest / total_num * 100

print(f'{p_musala:.2f}%')
print(f'{p_monblan:.2f}%')
print(f'{p_kilimanjaro:.2f}%')
print(f'{p_k2:.2f}%')
print(f'{p_everest:.2f}%')
