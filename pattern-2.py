def inverted_star_triangle(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

inverted_star_triangle(5)