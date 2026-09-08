binary = input("Enter a binary number: ")

decimal = 0
power = 0

for digit in reversed(binary):

    if digit != '0' and digit != '1':
        print("Invalid binary number")
        break

    decimal += int(digit) * (2 ** power)
    power += 1
else:
    print("Decimal:", decimal)