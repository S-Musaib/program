# 81. Inverted right-aligned triangle

n = int(input("Enter number of rows: "))

for i in range(n, 0, -1):
    # Spaces before stars
    for j in range(n - i):
        print(" ", end="")

    # Stars
    for j in range(i):
        print("*", end="")

    print()
