# 98. Alphabet triangle

n = int(input("Enter number of rows: "))

for i in range(n):

    letter = chr(65 + i)

    for j in range(i + 1):
        print(letter, end=" ")

    print()
