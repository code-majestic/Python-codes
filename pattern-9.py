# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# Half Diamond Star Pattern

rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(rows - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()