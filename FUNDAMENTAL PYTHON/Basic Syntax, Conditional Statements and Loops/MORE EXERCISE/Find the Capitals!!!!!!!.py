word = input()
digits = len(word)
word_list = []
for i in range(digits):
    if word[i].isupper():
        word_list.append(i)
    else:
        continue


print(word_list)

