loses_war = int(input())
price_helmet = float(input())
price_sword = float(input())
price_shield = float(input())
price_armor = float(input())
helmet = 1
sword = 1
shield = 1
armor = 1
shield_count = 0
costs = 0
for i in range(1,loses_war+1):
    if i % 2 == 0:
        helmet = 0
        costs += price_helmet
    if i % 3 == 0:
        sword = 0
        costs += price_sword
    if helmet == 0 and sword == 0:
        shield = 0
        costs += price_shield
        shield_count += 1
    if shield_count % 2 == 0 and shield_count > 0:
        costs += price_armor
        shield_count = 0
    helmet = 1
    sword = 1
    shield = 1
    armor = 1

print(f"Gladiator expenses: {costs:.2f} aureus")