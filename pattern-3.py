def right_aligned_star(n):
    for i in range(1, n + 1):
        for space in range(n - i):
            print(" ", end=" ")
        for star in range(i):
            print("*", end=" ")
        print()
right_aligned_star(5)