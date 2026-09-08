# 107. Spiral number matrix

n = 4

matrix = [[0 for j in range(n)] for i in range(n)]

top = 0
bottom = n - 1
left = 0
right = n - 1

number = 1

while top <= bottom and left <= right:

    # Left to right
    for j in range(left, right + 1):
        matrix[top][j] = number
        number += 1

    top += 1

    # Top to bottom
    for i in range(top, bottom + 1):
        matrix[i][right] = number
        number += 1

    right -= 1

    # Right to left
    if top <= bottom:
        for j in range(right, left - 1, -1):
            matrix[bottom][j] = number
            number += 1

        bottom -= 1

    # Bottom to top
    if left <= right:
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = number
            number += 1

        left += 1


# Print matrix
for i in range(n):
    for j in range(n):
        print(f"{matrix[i][j]:2}", end=" ")

    print()
