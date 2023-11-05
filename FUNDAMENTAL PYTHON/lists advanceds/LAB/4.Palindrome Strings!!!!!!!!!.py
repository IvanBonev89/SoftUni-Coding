def palindrome(words):
    palindromes = []
    counter = 0
    for word in words:
        if word == ''.join(reversed(word)):
            palindromes.append(word)
        if word == palindrome_text:
            counter += 1
    print(palindromes)
    print(f"Found palindrome {counter} times")


words = input().split()
palindrome_text = input()
palindrome(words)
