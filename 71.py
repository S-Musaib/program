n = int(input("Enter a decimal number: "))

if n == 0:
    binary = "0"
else:
    binary = ""

    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n //= 2

print("Binary:", binary)
