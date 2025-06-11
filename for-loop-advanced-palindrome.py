rows = 5

print("Advanced Palindrome Triangle Pattern:\n")
for i in range(1, rows + 1):
    # Print spaces
    for j in range(1, rows - i + 1):
        print(" ", end="")

    # Print descending numbers
    for j in range(i, 0, -1):
        print(j, end="")

    # Print ascending numbers
    for j in range(2, i + 1):
        print(j, end="")

    print()