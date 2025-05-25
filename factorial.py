# Method 1: Using a simple loop
def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Method 2: Using recursion
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Method 3: Using math.factorial() built-in function
import math

# Calculate 5! using all three methods
n = 5

result1 = factorial_loop(n)
result2 = factorial_recursive(n)
result3 = math.factorial(n)

print(f"5! using loop method: {result1}")
print(f"5! using recursive method: {result2}")
print(f"5! using math.factorial(): {result3}")

# Show the calculation step by step
print(f"\nStep by step: 5! = 5 × 4 × 3 × 2 × 1 = {result1}")