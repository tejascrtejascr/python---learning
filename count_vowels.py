text = input("Enter a word: ")

count = 0

for letter in text:
    if letter in "aeiouAEIOU":
        count += 1

print("Number of vowels:", count)