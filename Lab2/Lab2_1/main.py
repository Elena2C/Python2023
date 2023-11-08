def fibonacci(m):
    fibonacci_numbers = []

    a, b = 0, 1

    for _ in range(m):
        fibonacci_numbers.append(a)
        a, b = b, a + b

    return fibonacci_numbers


# Test case
n = 10
result = fibonacci(n)
print(f"The first {n} Fibonacci numbers are: {result}")
