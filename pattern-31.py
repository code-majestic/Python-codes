rows = 10
for i in range(rows):
    for j in range(rows):
        if i == j or j == rows - i-1 :
            print("*", end=" ")
        else:
            print("", end="")
    print()