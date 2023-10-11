def count_words(text):
    # Split the text into words using spaces as separators
    words = text.split()

    # Return the count of words
    return len(words)

# Example usage:
text = "I have Python exam "
word_count = count_words(text)
print(f"The text has {word_count} words.")
