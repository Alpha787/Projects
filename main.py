import random

def good_password_generator(lenght=16):
    letters = 'abcdefghijklmopqrstuvwxyz'
    upper_letter ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = '01234567890'
    symbols = '!@#$%^&*()_+-=\'\\"'

    alphabet = letters + upper_letter + digits + symbols

    password = ''
    for i in range(lenght):
        char = random.choice(alphabet)
        password += char

    return password

popular_passwords = """password
123456
12345678
1234
qwerty
12345
dragon
pussy
baseball
football"""
popular_password = popular_passwords.split('\n')
counter = 0

def bad_password_generator():
    global counter
    password = popular_password[counter]
    counter += 1
    if len(counter) >= len(popular_password):
        return password

print(good_password_generator())

for i in range(15):
    print(bad_password_generator())


