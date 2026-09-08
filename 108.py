# 108. Right arrow pattern

n = int(input("Enter number of rows in upper half: "))

# Upper half
for i in range(1, n + 1):

    print("*", end="")

    for j in range(i):
        print(" *", end="")

    print()

# Lower half
for i in range(n - 1, 0, -1):

    print("*", end="")

    for j in range(i):
        print(" *", end="")

    print()
