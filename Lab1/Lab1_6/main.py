def is_palindrome(number):
    # convert to string
    number_str = str(number)

    # check is same backwards
    return number_str == number_str[::-1]


# Example usage:
number = 100
result = is_palindrome(number)
if result:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
