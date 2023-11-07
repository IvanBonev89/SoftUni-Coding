n = int(input())
dictionary = {}
for i in range(1,n+1):
    register2 = input()
    register = register2.split()
    if register[0] != "unregister":
        name = register[1]
        registration = register[2]
        if name not in dictionary:
            print(f"{name} registered {registration} successfully")
            dictionary[name] = registration
        else:
            print(f"ERROR: already registered with plate number {dictionary[name]}")
    else:
        name = register[1]
        if name in dictionary:
            dictionary.pop(name)
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

for name, registration in dictionary.items():
    print(f"{name} => {registration}")