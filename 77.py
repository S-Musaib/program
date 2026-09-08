def increasing_decreasing(n):

    if n == 0:
        return

    increasing_decreasing(n - 1)

    print(n, end=" ")


n = int(input("Enter N: "))

# Increasing part
for i in range(1, n + 1):
    print(i, end=" ")

# Decreasing part using the same recursive function
def decreasing(n):

    if n == 0:
        return

    print(n, end=" ")
    decreasing(n - 1)


decreasing(n)

print()
