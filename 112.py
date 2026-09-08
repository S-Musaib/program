# 112. Square with diagonals marked

n = int(input("Enter size: "))

for i in range(n):

    for j in range(n):

        # Border
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")

        # Main diagonal
        elif i == j:
            print("*", end=" ")

        # Other diagonal
        elif i + j == n - 1:
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print()
