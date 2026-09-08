# 104. Hollow diamond inside rectangle

n = int(input("Enter size: "))

# Total width
width = 2 * n - 1

for i in range(1, n + 1):

    for j in range(width):

        left = n - i
        right = n + i - 2

        if j == left or j == right or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

# Lower half
for i in range(n - 1, 0, -1):

    for j in range(width):

        left = n - i
        right = n + i - 2

        if j == left or j == right:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()
