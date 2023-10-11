def camel_to_snake(string):
    result = [string[0].lower()]
    for char in string[1:]:
        if char.isupper():
            result.extend(['_', char.lower()])
        else:
            result.append(char)
    return ''.join(result)


upper_camel_case = input("Enter a string in UpperCamelCase: ")

snake_case = camel_to_snake(upper_camel_case)
print("Converted to lowercase_with_underscores:", snake_case)
