# 110. Plus pattern

n = int(input("Enter an odd number: "))

middle = n // 2

for i in range(n):

    for j in range(n):

        if i == middle or j == middle:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()
