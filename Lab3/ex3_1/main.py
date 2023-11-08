def set_operations(a, b):
    intersection = set(a) & set(b)
    union = set(a) | set(b)
    difference_a_b = set(a) - set(b)
    difference_b_a = set(b) - set(a)

    result = [intersection, union, difference_a_b, difference_b_a]
    return result


# Example usage:
list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]

result = set_operations(list_a, list_b)
print(result)
