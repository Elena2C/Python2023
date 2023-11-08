def lists_(*lists):
    max_length = max(len(lst) for lst in lists)
    result = []

    for i in range(max_length):
        tuple_items = ()
        for lst in lists:
            if i < len(lst):
                tuple_items += (lst[i],)
            else:
                tuple_items += (None,)
        result.append(tuple_items)

    return result


# Test case
list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = ["a", "b", "c"]

result = lists_(list1, list2, list3)
print("Result:", result)
