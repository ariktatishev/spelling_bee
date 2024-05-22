from english_words import get_english_words_set
import re


def create_word_set(file_path):
    """
    Creates a set of words from the given file.
    Excludes lines with asterisks and extracts only
    the alphabetical part of each line.

    :param file_path: Path to the text file containing words.
    :return: A set of words without any asterisks and numbers.
    """
    word_set = set()
    with open(file_path, 'r') as file:
        for line in file:
            if '*' not in line:
                # Use regex to find all alphabetical characters up to the
                # first non-alphabetical character
                match = re.match(r'^[A-Za-z]+', line.strip())
                if match:
                    word = match.group(0)
                    word_set.add(word.lower())
    return word_set


def get_words(letters, specific_letter: str):
    # The set of letters you're interested in
    letter_set = set(letters)

    # Get the set of English words
    add_english_words1 = get_english_words_set(["web2"], lower=True)
    add_english_words2 = get_english_words_set(["gcide"], lower=True)
    add_english_words = set(
        [word for word in add_english_words1 if word in add_english_words2])
    english_words = create_word_set("db.txt")

    # Filter the words based on your criteria
    filtered_words = [
        word for word in english_words
        if len(word) >= 4 and specific_letter in word and all(
            char in letter_set for char in word)
    ]
    add_filtered_words = [
        word for word in add_english_words
        if len(word) >= 4 and specific_letter in word
        and word not in filtered_words and all(char in letter_set
                                               for char in word)
    ]
    sorted_filtered_words = sorted(filtered_words)
    sorted_add_filtered_words = sorted(add_filtered_words)
    table = []
    for word in sorted_filtered_words:
        table.append([
            word,
            len(set(word)) == 7,
            len(word), 1 if len(word) == 4 else len(word)
        ])
    add_table = []
    for word in sorted_add_filtered_words:
        add_table.append([
            word,
            len(set(word)) == 7,
            len(word), 1 if len(word) == 4 else len(word)
        ])
    return table, add_table
