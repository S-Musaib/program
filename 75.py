def is_palindrome(text, start, end):

    if start >= end:
        return True

    if text[start] != text[end]:
        return False

    return is_palindrome(text, start + 1, end - 1)


text = input("Enter a string: ")

if is_palindrome(text, 0, len(text) - 1):
    print("Palindrome")
else:
    print("Not a palindrome")