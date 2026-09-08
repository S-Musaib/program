a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

original_a = a
original_b = b

a = abs(a)
b = abs(b)

x = a
y = b

while y != 0:
    x, y = y, x % y

gcd = x

if gcd == 0:
    lcm = 0
else:
    lcm = abs(original_a * original_b) // gcd

print("LCM:", lcm)
