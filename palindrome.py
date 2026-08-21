text = input("Enter a word or number: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")