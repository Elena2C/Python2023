def spiral_order(matrix):
    if not matrix:
        return ""

    result = []
    while matrix:
        # Traverse the top row
        result.extend(matrix[0])
        matrix.pop(0)

        if matrix and matrix[0]:
            # Traverse the right column
            for row in matrix:
                result.append(row[-1])
                row.pop(-1)

        if matrix:
            # Traverse the bottom row
            result.extend(matrix[-1][::-1])
            matrix.pop(-1)

        if matrix and matrix[0]:
            # Traverse the left column
            for row in matrix[::-1]:
                result.append(row[0])
                row.pop(0)

    return ''.join(result)

# Example matrix
matrix = [
    ['f', 'i', 'r', 's'],
    ['n', '_', 'l', 't'],
    ['o', 'b', 'a', '_'],
    ['h', 't', 'y', 'p']
]

result = spiral_order(matrix)
print(result)
