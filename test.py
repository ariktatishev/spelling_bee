from english_words import get_english_words_set

# The set of letters you're interested in
letters = set('cflnuia')

# Get the set of English words
english_words = get_english_words_set(["web2"], lower=True)

# Filter the words based on your criteria
filtered_words = [word for word in english_words if len(word) >= 4 and 'f' in word and all(char in letters for char in word)]

# Print or use the filtered words as needed
sorted_filtered_words = sorted(filtered_words)

for word in sorted_filtered_words:
    print(word)
