rows = 5

for i in range(1, rows + 1):
    for space in range(rows - i):
        print(" ", end="")
    for j in range(1, i + 1):
        if i >= j:
            if j % 2 == 0:
                print("*", end=" ")
            else:
                print("*", end=" ")
    print()

for i in range(rows - 1, 0, -1):
    for space in range(rows - i):
        print(" ", end="")
    for j in range(1, i + 1):
        if i >= j:
            if j % 2 == 0:
                print("*", end=" ")
            else:
                print("*", end=" ")
    print()