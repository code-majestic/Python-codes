rows = 5
ch = 65  
for i in range(rows):
    for j in range(rows):
        if j == rows - i - 1:
            print(chr(ch + i), end="")
        else:
            print(" ", end="")
    print()