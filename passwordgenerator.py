import random
import string
charecters = string.ascii_letters + string.digits + string.punctuation

password_length = int(input("Password Length:"))

def generate_password(length):
    return "".join(random.choices(charecters, k=password_length))

print(generate_password(password_length))