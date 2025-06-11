n = 10
a, b = 0, 1
count = 0

print(f"Fibonacci Series up to {n} terms (using while loop):")

while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1