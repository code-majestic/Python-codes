def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

terms = 10
print(f"Fibonacci Series up to {terms} terms (using recursion):")
for i in range(terms):
    print(fibonacci(i), end=" ")