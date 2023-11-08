def compare_dicts(dict1, dict2):
    if type(dict1) != type(dict2):
        return False

    if isinstance(dict1, dict):
        if len(dict1) != len(dict2):
            return False
        for key in dict1:
            if key not in dict2:
                return False
            if not compare_dicts(dict1[key], dict2[key]):
                return False
    elif isinstance(dict1, (list, set, tuple)):
        if len(dict1) != len(dict2):
            return False
        for elem1, elem2 in zip(dict1, dict2):
            if not compare_dicts(elem1, elem2):
                return False
    else:
        if dict1 != dict2:
            return False

    return True


# Example usage:
dict1 = {'a': { 'd' : 1}, 'b': [1, 2, 3], 'c': {'x': 42, 'y': [1, 2]}}
dict2 = {'a': { 'd' : 1}, 'b': [1, 2, 3], 'c': {'x': 42, 'y': [1, 2]}}
dict3 = {'a': 1, 'b': [1, 2, 4], 'c': {'x': 42, 'y': [1, 2]}}

print(compare_dicts(dict1, dict2))
print(compare_dicts(dict1, dict3))
