x = int(input("Enter x: "))
n = int(input("Enter n: "))

result = 1

if n >= 0:
    for i in range(n):
        result *= x
else:
    for i in range(-n):
        result *= x

    result = 1 / result

print("Power:", result)