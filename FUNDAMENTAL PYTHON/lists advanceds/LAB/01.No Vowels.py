def remove_vowels(text):
    new_text = ''.join([char for char in text if char.lower() not in ['a', 'o', 'u', 'e', 'i']])
    return new_text

text = input()
print(remove_vowels(text))