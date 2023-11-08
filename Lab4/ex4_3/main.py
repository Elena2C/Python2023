class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def get(self, row, col):
        return self.data[row][col]

    def set(self, row, col, value):
        self.data[row][col] = value

    def transpose(self):
        transposed = Matrix(self.columns, self.rows)
        for i in range(self.rows):
            for j in range(self.columns):
                transposed.set(j, i, self.get(i, j))
        return transposed

    def matrix_multiply(self, other_matrix):
        if self.columns != other_matrix.rows:
            raise ValueError("Matrix dimensions are incompatible for multiplication")

        result = Matrix(self.rows, other_matrix.columns)
        for i in range(result.rows):
            for j in range(result.columns):
                dot_product = sum(self.get(i, k) * other_matrix.get(k, j) for k in range(self.columns))
                result.set(i, j, dot_product)
        return result

    def iterate(self):
        for i in range(self.rows):
            for j in range(self.columns):
                yield i, j, self.get(i, j)

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])


# Example usage with corrected dimensions for matrix multiplication:
matrix = Matrix(2, 3)
matrix.set(0, 0, 1)
matrix.set(0, 1, 2)
matrix.set(0, 2, 3)
matrix.set(1, 0, 4)
matrix.set(1, 1, 5)
matrix.set(1, 2, 6)

print("Original Matrix:")
print(matrix)

# Transpose
transpose = matrix.transpose()
print("\nTransposed Matrix:")
print(transpose)

# Matrix Multiplication
matrix2 = Matrix(3, 2)
matrix2.set(0, 0, 7)
matrix2.set(0, 1, 9)
matrix2.set(1, 0, 8)
matrix2.set(1, 1, 10)
matrix2.set(2, 0, 11)
matrix2.set(2, 1, 12)

result = matrix.matrix_multiply(matrix2)
print("\nFirst matrix")
print(matrix)
print("\nSecond matrix")
print(matrix2)
print("\nMatrix Multiplication Result:")
print(result)


# Iterate through elements
print("\nIterating through elements:")
for i, j, value in matrix.iterate():
    print(f"Element at ({i}, {j}): {value}")
