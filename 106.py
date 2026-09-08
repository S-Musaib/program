# 106. Zigzag pattern

n = int(input("Enter number of columns: "))

# First row
for i in range(n):
    print("*", end=" ")

print()

# Middle star
for i in range(n - 1):
    print("  ", end=" ")

print("*")

# Last row
for i in range(n):
    print("*", end=" ")

print()
