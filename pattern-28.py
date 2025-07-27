rows = 5
ch = 65
for i in range(rows):
    for j in range(rows - 1, -1, -1):
        if i == j:
            print(chr(ch), end="")
        else:
            print(" ", end="")
    print()
    ch += 1