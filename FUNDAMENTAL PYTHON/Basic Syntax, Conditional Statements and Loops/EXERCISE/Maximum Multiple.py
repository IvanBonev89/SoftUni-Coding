n1 = int(input())
n2 = int(input())
secret_number = 0
last_secret = 0

for i in range(n2, n1-1, -1):
    if i % n1 == 0:
        secret_number = i
        if secret_number >= last_secret:
          last_secret = secret_number
print(last_secret)

