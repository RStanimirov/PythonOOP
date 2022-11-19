def print_row(size, stars):
    for _ in range(size - stars):
        print(" ", end="")
    for _ in range(1, stars):
        print("*", end=" ")
    print("*")


n = int(input())
for i in range(1, n):
    print_row(n, i)
for j in range(n, 0, -1):
    print_row(n, j)
