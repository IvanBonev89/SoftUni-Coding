animal = input()

queue = animal.split(", ")

# print(len(queue))  broq dumite taka v LIST
# ako e len(animal) shte broi bukvite
# print(len(animal))

wolf_index = queue.index("wolf")
last_symbol = len(queue) -1
#last_symbol = queue[-1]
#if last_symbol == "wolf":
if last_symbol == wolf_index:
    print("Please go away and stop eating my sheep")
else:
    sheep_position = animal.count("sheep")

    print("Oi! Sheep number {}! You are about to be eaten by a wolf!".format(sheep_position))
