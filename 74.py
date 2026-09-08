x = float(input("Enter x in radians: "))
n = int(input("Enter number of terms: "))

total = 0
factorial = 1
power = x

for i in range(n):

    exponent = 2 * i + 1

    # Calculate factorial of exponent
    factorial = 1

    for j in range(1, exponent + 1):
        factorial *= j

    term = power / factorial

    if i % 2 == 0:
        total += term
    else:
        total -= term

    power *= x * x

print("Sin series result:", total)