from Ex_94 import generate_password
from Ex_96 import goodpassword_generator


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