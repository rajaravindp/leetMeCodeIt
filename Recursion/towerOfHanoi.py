def tower_of_hanoi(n, a, b, c):
    if n > 0:
        tower_of_hanoi(n-1, a, c, b)
        print(f"{a} to {c}")
        tower_of_hanoi(n-1, b, a, c)

print(tower_of_hanoi(3, 1, 2, 3))
