import random
import string

pass_len = int(input("Enter length of Password required: "))
charValues = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(charValues)

print("Password:", password)
