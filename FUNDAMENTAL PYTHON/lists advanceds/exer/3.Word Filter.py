
words = input().split()
filted = [w for w in words if len(w) % 2 == 0]
print("\n".join(filted))
