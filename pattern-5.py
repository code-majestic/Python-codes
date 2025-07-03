#          *
#         ***
#        *****
#       *******
#      *********   
# Pyramid pattern
rows = 5
for i in range(1, rows + 1):
    # spaces
    for space in range(rows - i):
        print(" ", end="")
    # stars
    for star in range(2 * i - 1):
        print("*", end="")
    print()
