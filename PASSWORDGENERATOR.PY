import random
import string
# CODE FOR PASSWORD GENERATOR 
def generate_password(length=8):
    if length < 6:
        print("MINUIMUM LENGTH OF PASSWORD SHOULD BE 6.")
        return ""

    low = string.ascii_lowercase
    upp = string.ascii_uppercase
    digit = string.digits
    symb = string.punctuation
    password = [
        random.choice(low),
        random.choice(upp),
        random.choice(digit),
        random.choice(symb)
    ]

    all_chars = low + upp + digit + symb
    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)

    return ''.join(password)
length = int(input("Enter password length: "))
password = generate_password(length)
print("Generated Password:", password)
