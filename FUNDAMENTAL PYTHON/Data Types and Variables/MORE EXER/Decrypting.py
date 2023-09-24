key = int(input())
n = int(input())

decrypted_message = ""

for i in range(n):
  line = input()
  for character in line:

      decrypted_message += chr(ord(character) + key)

print(decrypted_message)