# n = int(input())
#
# for i in range(1, n + 1):
#     for j in range(1, n - i + 1):
#         print(end=' ')
#     for k in range(0, 2 * i - 1):
#         print('*', end='')
#     print()
#
# for i in range(1, n):
#     for j in range(1, i + 1):
#         print(end=' ')
#     for k in range(1, (2 * (n - i))):
#         print('*', end='')
#     print()

n = int(input())

for i in range(1, n):
    for j in range(n - i):
        print(".", end="")
    for k in range(1, i):
        print("*", end=".")
    print('*')

for i in range(n, 0, -1):
    for j in range(n - i):
        print(".", end="")
    for k in range(1, i):
        print("*", end=".")
    print('*')

