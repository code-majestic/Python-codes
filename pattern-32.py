rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        if i % 2 == 0:
            print("*", end="")
        else:
            print(i, end="")
    print()