rows = 5
for i in range(rows):
    for j in range(rows):
        if i == j or j == rows - i - 1:
            print("*", end="")
        elif i == 0 or i == rows-1 or j == 0 or j == rows-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()