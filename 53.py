def product_of_digits(n):
    n = abs(n)

    if n < 10:
        return n

    return (n % 10) * product_of_digits(n // 10)


n = int(input("Enter a number: "))

if n == 0:
    result = 0
else:
    result = product_of_digits(n)

print("Product of digits:", result)