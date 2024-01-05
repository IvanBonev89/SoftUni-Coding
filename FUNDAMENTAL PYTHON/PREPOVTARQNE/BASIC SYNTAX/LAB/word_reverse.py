word = input()
reverse_word = ""

for alpha in range(len(word) -1,-1,-1):
    reverse_word += word[alpha]
print(reverse_word)