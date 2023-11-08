def validate_dict(rules, input_dict):
    for key, prefix, middle, suffix in rules:
        if key not in input_dict:
            return False

        value = input_dict[key]

        if not value.startswith(prefix):
            return False

        if middle not in value[1:-1]:
            return False

        if not value.endswith(suffix):
            return False

    return True


# Example usage:
rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
input_dict = {"key1": "come inside, it's too cold out", "key2": "start of winter", "key3": "this is not valid"}

result = validate_dict(rules, input_dict)
print(result)
