rows = 5
for i in range(rows):
    for j in range(rows):
        if i == 0 or i == rows - 1 or j == rows - i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()