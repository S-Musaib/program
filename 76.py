def count_vowels(text, index):

    if index == len(text):
        return 0

    if text[index].lower() in "aeiou":
        return 1 + count_vowels(text, index + 1)
    else:
        return count_vowels(text, index + 1)


text = input("Enter a string: ")

count = count_vowels(text, 0)

print("Number of vowels:", count)
