def count_matching_arguments(*args, **kwargs):
    values_set = set(kwargs.values())
    count = sum(1 for arg in args if arg in values_set)
    return count


# Example usage:
result = count_matching_arguments(1, 2, 3, 4, x=1, y=2, z=3, w=5)
print(result)
