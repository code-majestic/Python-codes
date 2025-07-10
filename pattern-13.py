rows = 5

for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(" ", end=" ")
    for k in range(1, i + 1):
        if i >= k:
            print(k, end="  ",)
    print()