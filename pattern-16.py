rows = 5
print("Pattern 1: Hollow Full Pyramid")
for i in range(1, rows + 1):
    for space in range(rows - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print("\n")
