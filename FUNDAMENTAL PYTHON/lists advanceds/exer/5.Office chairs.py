rooms = int(input())
total_free_chairs = 0

for room_number in range(1, rooms + 1):
    chairs_peoples = input().split()
    chairs = chairs_peoples[0].count("X")
    visitors = int(chairs_peoples[1])

    if visitors > chairs:
        need = visitors - chairs
        total_free_chairs -= need
        print(f"{need} more chairs needed in room {room_number}")
    else:
        free = chairs - visitors
        total_free_chairs += free

if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")