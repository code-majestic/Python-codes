rows = 3
for i in range(rows):
    for j in range(rows):
        if i == rows // 2 or j == rows // 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()