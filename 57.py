n = int(input("Enter N: "))

for number in range(2, n + 1):

    is_prime = True

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, end=" ")

print()