rows = 5
for i in range(rows):
    for j in range(rows):
        if i == 0 or i == rows - 1:
            print(j + 1, end="")
        elif j == rows - i - 1:
            print(3, end="")
        else:
            print(" ", end="")
    print()