# noinspection PyShadowingNames

def list_operations(a, b):
    intersection = list(set(a) & set(b))

    union = list(set(a) | set(b))

    a_minus_b = list(set(a) - set(b))

    b_minus_a = list(set(b) - set(a))

    return intersection, union, a_minus_b, b_minus_a


# Test case
list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

intersection, union, a_minus_b, b_minus_a = list_operations(list_a, list_b)

print("Intersection:", intersection)
print("Union:", union)
print("Elements in list_a but not in list_b:", a_minus_b)
print("Elements in list_b but not in list_a:", b_minus_a)
