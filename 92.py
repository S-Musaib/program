# 92. Pascal's triangle

n = int(input("Enter number of rows: "))

for i in range(n):

    # Spaces
    for j in range(n - i - 1):
        print(" ", end=" ")

    value = 1

    for j in range(i + 1):

        print(value, end="   ")

        # Calculate next value
        value = value * (i - j) // (j + 1)

    print()
