count = 0
total = 0

while True:

    n = int(input("Enter a number (-1 to stop): "))

    if n == -1:
        break

    total += n
    count += 1

if count > 0:
    average = total / count
    print("Count:", count)
    print("Average:", average)
else:
    print("No numbers were entered.")