n = int(input())

# 1) print the top part:
#    *
#   * *
#  * * *
# * * * *
space = n - 1
for i in range(0, n):
    for j in range(0, space):
        print(" ", end="")
    for k in range(0, i+1):
        print("*", end=" ")
    space -= 1
    print()

# 2) print the bottom part:
#  * * *
#   * *
#    *
space = 1
for i in range(n-1, 0, -1):
    for j in range(0, space):
        print(" ", end="")
    for k in range(0, i):
        print("*", end=" ")
    space += 1
    print()
