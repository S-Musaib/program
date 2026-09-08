n = int(input("Enter a number: "))

original = n
n = abs(n)

digits = len(str(n))
total = 0
temp = n

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
