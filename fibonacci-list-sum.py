n = 10
fib_list = []
a, b = 0, 1

for _ in range(n):
    fib_list.append(a)
    a, b = b, a + b

print(f"Fibonacci List: {fib_list}")
print(f"Sum of Fibonacci series: {sum(fib_list)}")