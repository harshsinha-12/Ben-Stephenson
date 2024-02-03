from Ex_96 import goodpassword_generator
import random

def generate_password():
    length = random.randint(8, 12)  # Password length between 8 and 12 characters
    password = []

    while len(password) < length:
        char = chr(random.randrange(65, 127))
        password.append(char)

    # Ensuring the password meets the criteria
    if not any(char.isdigit() for char in password):
        password[random.randint(0, len(password) - 1)] = str(random.randint(0, 9))
    if not any(char.isupper() for char in password):
        password[random.randint(0, len(password) - 1)] = chr(random.randint(65, 90))
    if not any(char.islower() for char in password):
        password[random.randint(0, len(password) - 1)] = chr(random.randint(97, 122))

    return ''.join(password)



def count_trials():
    count = 0
    while True:
        count += 1
        password = generate_password()
        if goodpassword_generator(password):
            return count, password

def main():
    count, password = count_trials()
    print(f"It took {count} trials to generate a good password.")
    print(f"The generated password is: {password}")

main()