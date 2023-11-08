def is_palindrome(number):
    num_str = str(number)

    return num_str == num_str[::-1]


def count_palindromes_and_find_max(numbers):
    count = 0
    max_palindrome = None

    for num in numbers:
        if is_palindrome(num):
            count += 1
            if max_palindrome is None or num > max_palindrome:
                max_palindrome = num

    return count, max_palindrome


# Test case
numbers_ = [121, 123, 1331, 12321]
result = count_palindromes_and_find_max(numbers_)
print("Number of palindromes:", result[0])
print("Greatest palindrome number:", result[1])
