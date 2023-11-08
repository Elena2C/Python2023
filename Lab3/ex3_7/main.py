from itertools import combinations


def set_operations(*sets):
    result = {}

    for set1, set2 in combinations(sets, 2):
        key = f"{set1} | {set2}"
        result[key] = set1 | set2

        key = f"{set1} & {set2}"
        result[key] = set1 & set2

        key = f"{set1} - {set2}"
        result[key] = set1 - set2

        key = f"{set2} - {set1}"
        result[key] = set2 - set1

    return result


# Example usage:
set1 = {1, 2}
set2 = {2, 3}

result = set_operations(set1, set2)
for key, value in result.items():
    print(f"{key}: {value}")
