words = input().split()

# Create a dictionary to store the frequency of each word, case-insensitive
word_counts = {}
for word in words:
    word_lower = word.lower()
    if word_lower not in word_counts:
        word_counts[word_lower] = 1
    else:
        word_counts[word_lower] += 1

# Print all words that occur an odd number of times
for word, count in word_counts.items():
    if count % 2 != 0:
        print(word, end=' ')
