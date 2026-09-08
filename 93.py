# 93. Number pyramid

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):

    # Spaces
    for j in range(n - i):
        print("  ", end="")

    # Numbers from 1 to 2*i-1
    for j in range(1, 2 * i):
        print(j, end=" ")

    print()
