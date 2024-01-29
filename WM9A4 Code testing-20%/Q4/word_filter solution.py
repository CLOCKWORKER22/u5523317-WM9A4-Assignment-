def word_filter_counter(text, filter_words):
    # Convert the text to lowercase for case-insensitive comparison
    text_lower = text.lower()

    # Remove punctuation marks and split the text into words
    words = ''.join(c if c.isalnum() or c.isspace() else ' ' for c in text_lower).split()

    # Initialize a dictionary to store the counts of filtered words
    word_counts = {}

    # Iterate through the words and count the occurrences of filtered words
    for word in words:
        if word in filter_words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

    return word_counts


text = input("please enter paragraph here")
filter_words = ["we", "the", "or""we", "the", "or"]
result = word_filter_counter(text, filter_words)
print(result)
