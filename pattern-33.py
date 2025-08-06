rows = 5
for i in range(rows):
    for j in range(rows):
        if (i + j) % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()