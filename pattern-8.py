# Floyd's Triangle

# 1
# 2 3
# 4 5 6
# 7 8 9 10

rows = 4
num = 1
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()
