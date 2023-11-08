def order_tuples_by_third_char(tuples_list):
    def custom_key(tuple_item):
        if len(tuple_item) >= 2:
            second_element = tuple_item[1]
            if len(second_element) >= 3:
                return second_element[2]
        return ''

    sorted_tuples = sorted(tuples_list, key=custom_key)

    return sorted_tuples


# Test case
tuples_list = [('abc', 'bcd'), ('abc', 'zza')]

result = order_tuples_by_third_char(tuples_list)
print("Ordered tuples:", result)
