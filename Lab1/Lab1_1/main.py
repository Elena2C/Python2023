def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_gcd_of_numbers(numbers):
    if len(numbers) < 2:
        return 1  # Return None for invalid input
    gcd = numbers[0]
    for num in numbers[1:]:
        gcd = find_gcd(gcd, num)
    return gcd

input_str = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in input_str.split()]

result = find_gcd_of_numbers(numbers)

if result is None:
    print("At least two numbers are required to find the GCD.")
else:
    print("The greatest common divisor (GCD) of the numbers is:", result)
