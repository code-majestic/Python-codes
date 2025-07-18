rows = 5
for i in range(1, rows + 1):
    for j in range(rows, 0, -1):
        if i == j:
            print(i, end="")
        else:
            print(" ", end="")
    print()