
import random
import string

password = ""

for i in range(8):
    password += random.choice(string.ascii_letters)

print("Your password:", password)

