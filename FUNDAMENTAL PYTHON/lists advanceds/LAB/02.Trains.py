def trains (numbers,command):
    list_wagons = [0] * numbers_of_wagons
    while True:
        command = input().split()
        if command[0] == "End":
            break
        if command[0] == "add":
                list_wagons[-1] += (int(command[1]))
        elif command[0] == "insert":
            index = int(command[1])
            people = int(command[2])
            list_wagons[index] += people
        elif command[0] == "leave":
            index = int(command[1])
            people = int(command[2])
            list_wagons[index] -= people
    return list_wagons



command = ''
numbers_of_wagons = int(input())
print(trains(numbers_of_wagons, command))
