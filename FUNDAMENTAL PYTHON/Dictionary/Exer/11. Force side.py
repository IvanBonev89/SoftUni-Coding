force_side_dictionary = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break
    else:
        if "->" in command:
            force_user, force_side = command.split(" -> ")

            # Remove force_user from any existing force side
            for value in force_side_dictionary.values():
                if force_user in value:
                    value.remove(force_user)
                    break

            # Add force_user to the specified force side
            if force_side not in force_side_dictionary.keys():
                force_side_dictionary[force_side] = []
            force_side_dictionary[force_side].append(force_user)

            # Print the joining message
            print(f"{force_user} joins the {force_side} side!")
        else:
            force_side, force_user = command.split(" | ")

            # Check if force_user already exists in any force side
            user_found = False
            for value in force_side_dictionary.values():
                if force_user in value:
                    user_found = True
                    break

            # If not found, add force_user to the specified force side
            if not user_found:
                if force_side not in force_side_dictionary.keys():
                    force_side_dictionary[force_side] = []
                force_side_dictionary[force_side].append(force_user)

# Print the force sides and their members
for force_side, force_users in force_side_dictionary.items():
    if len(force_users) > 0:
        print(f"Side: {force_side}, Members: {len(force_users)}")
        for force_user in force_users:
            print(f"! {force_user}")
