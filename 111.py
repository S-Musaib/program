# 111. Heart pattern

n = 6

# Upper part
for i in range(3):

    for j in range(3 - i):
        print(" ", end="")

    for j in range(2 * i + 1):
        print("*", end=" ")

    for j in range(3 - i):
        print(" ", end="")

    print()

# Lower part
for i in range(n, 0, -1):

    for j in range(n - i):
        print(" ", end="")

    for j in range(2 * i - 1):
        print("*", end=" ")

    print()
