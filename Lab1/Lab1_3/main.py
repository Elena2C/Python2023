def count_occurrences(substring, string):
    count = 0
    start = 0

    while True:
        start = string.find(substring, start)
        if start == -1:
            break
        count += 1
        start += 1

    return count

first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")


occurrence_count = count_occurrences(first_string, second_string)
print(f"The first string appears {occurrence_count} times in the second string.")
