import re


def extract_number(text):
    # Use a regular expression to find the first number in the text
    match = re.search(r'\d+', text)

    if match:
        # Extract the matched number
        number = int(match.group())
        return number
    else:
        # Return None if no number is found
        return None


# Example usage:
text1 = "An apple is 123 USD 56"
result1 = extract_number(text1)
print(f"Extracted number: {result1}")

text2 = "abc123abc"
result2 = extract_number(text2)
print(f"Extracted number: {result2}")
